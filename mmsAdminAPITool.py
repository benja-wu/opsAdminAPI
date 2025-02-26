## 
# Get the host and disk related metrics from Ops mms Admin API
# Write metrics into Mysql tables 
## 
import requests
import json
from requests.auth import HTTPDigestAuth
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Configurations
# Change it to your ops mms host
BASE_URL = "https://youropsmms.opsmanagerservers.mdbps.net:8443/api/public/v1.0"
# Change it to your group id 
GROUP_ID = "123"

# change it to your public key and private key
AUTH = HTTPDigestAuth("bbbb", "aaaa")
# change it to your self-sign CA file path 
CA_CERT_PATH = "/home/users/benjaminwu/ca.cert"

HEADERS = {"Content-Type": "application/json"}

# MySQL Connection Config
MYSQL_CONFIG = {
    "host": "localhost",    # the MySQL host
    "user": "root",         # the MySQL username
    "password": "password",  # the MySQL password
    "database": "metrics"  # the MySQL database
}

def convert_bytes(size_in_bytes):
    """
    Convert bytes to a human-readable format (GB, MB, KB).
    """
    if size_in_bytes >= 1 << 30:
        return f"{size_in_bytes / (1 << 30):.2f} GB"
    elif size_in_bytes >= 1 << 20:
        return f"{size_in_bytes / (1 << 20):.2f} MB"
    elif size_in_bytes >= 1 << 10:
        return f"{size_in_bytes / (1 << 10):.2f} KB"
    else:
        return f"{size_in_bytes} Bytes"

def convert_iso_to_mysql_datetime(iso_timestamp):
    """Convert ISO 8601 timestamp to MySQL DATETIME format."""
    try:
        return datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"Invalid timestamp format: {iso_timestamp}")
        return None  # Handle cases where conversion fails

# Function to fetch hosts
def fetch_hosts():
    """Fetch all hosts in the group."""
    url = f"{BASE_URL}/groups/{GROUP_ID}/hosts?pretty=true"
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=CA_CERT_PATH)
    response.raise_for_status()
    return response.json()

# Function to fetch disk partitions for a host
def fetch_disk_partitions(host_id):
    url = f"{BASE_URL}/groups/{GROUP_ID}/hosts/{host_id}/disks"
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=CA_CERT_PATH)
    response.raise_for_status()
    return response.json()



# Function to fetch disk measurements for a specific partition
def fetch_disk_measurements(host_id, partition_name):
    url = f"{BASE_URL}/groups/{GROUP_ID}/hosts/{host_id}/disks/{partition_name}/measurements"
    params = {
        "granularity": "PT12H",  # 12 hours
        "period": "P2D",         # 2 days
        "pretty": "true"
    }
    response = requests.get(url, auth=AUTH, headers=HEADERS, params=params, verify=CA_CERT_PATH)
    response.raise_for_status()
    return response.json()

def fetch_host_details(host_id):
    """Fetch details of a specific host."""
    url = f"{BASE_URL}/groups/{GROUP_ID}/hosts/{host_id}"
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=CA_CERT_PATH)
    response.raise_for_status()
    print("fetch details for host: ", host_id, " successfully\n")
    return response.json()

def fetch_host_disks(host_id):
    """Fetch disk information for a specific host."""
    url = f"{BASE_URL}/groups/{GROUP_ID}/hosts/{host_id}/disks"
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=CA_CERT_PATH)
    response.raise_for_status()
    print("fetch details for host disk: ", host_id, " successfully\n")
    return response.json()

def enrich_host_with_disk_data(host):
    host_id = host["id"]
    partition_name = "xvdb"  # Replace with actual partition name if different
    disk_data = fetch_disk_measurements(host_id, partition_name)
    
    # Extract relevant measurements
    measurements = disk_data.get("measurements", [])
    disk_info = {}
    for measurement in measurements:
        name = measurement.get("name")
        if name in ["DISK_PARTITION_SPACE_FREE", "DISK_PARTITION_SPACE_USED"]:
            # Get the latest data point
            data_points = measurement.get("dataPoints", [])
            if data_points:
                latest_data_point = data_points[-1]
                value_in_bytes = latest_data_point.get("value", 0)
                disk_info[name] = convert_bytes(value_in_bytes)
    
    # Add disk info to host data
    host["disk"] = disk_info
    return host

def insert_host_data(host_data):
    """Insert host data into MySQL."""
    connection = connect_db()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO hosts (host_id, host_name, version, ip_address, replica_set_name, type_name)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE host_name=%s, version=%s, ip_address=%s, replica_set_name=%s, type_name=%s;
        """
        data = (
            host_data["id"], host_data["hostname"], host_data["version"], 
            host_data["ipAddress"], host_data["replicaSetName"], host_data["typeName"],
            host_data["hostname"], host_data["version"], host_data["ipAddress"], 
            host_data["replicaSetName"], host_data["typeName"]
        )
        cursor.execute(insert_query, data)
        connection.commit()
        print(f"Inserted/Updated host: {host_data['hostname']}")
    except Error as e:
        print(f"Error inserting host data: {e}")
    finally:
        cursor.close()
        connection.close()

def insert_disk_metrics(host_id, host_name, disk_data):
    """Insert disk metrics into MySQL."""
    connection = connect_db()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO disk_metrics (host_id,host_name, partition_name, timestamp, space_used, space_free)
            VALUES (%s, %s,%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE space_used=%s, space_free=%s;
        """
        for partition in disk_data:
            partition_name = partition["partitionName"]
            space_used_list = partition.get("DISK_PARTITION_SPACE_USED", [])
            space_free_list = partition.get("DISK_PARTITION_SPACE_FREE", [])

            for i in range(len(space_used_list)):
                iso_timestamp = space_used_list[i]["timestamp"]
                timestamp = convert_iso_to_mysql_datetime(iso_timestamp)  # Convert timestamp
                space_used = space_used_list[i]["value"]
                space_free = space_free_list[i]["value"] if i < len(space_free_list) else "N/A"

                data = (host_id,host_name, partition_name, timestamp, space_used, space_free, space_used, space_free)
                cursor.execute(insert_query, data)

        connection.commit()
        print(f"Inserted disk metrics for host: {host_id}")
    except Error as e:
        print(f"Error inserting disk metrics: {e}")
    finally:
        cursor.close()
        connection.close()

def connect_db():
    """Create MySQL connection."""
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def main():
    try:
        # Fetch hosts data
        hosts_data = fetch_hosts()
        
        # Iterate over each host to fetch and append disk measurements
        for host in hosts_data.get("results", []):
            host_id = host.get("id")
            if not host_id:
                    continue
            host_name = host.get("hostname")
            # Extract key host details
            host_info = {
                "id": host_id,
                "hostname": host_name,
                "version": host.get("version"),
                "ipAddress": host.get("ipAddress"),
                "replicaSetName": host.get("replicaSetName"),
                "typeName": host.get("typeName"),
            }

            # record the metrics into MySQL 
            insert_host_data(host_info)

            # Fetch disk partitions for the host
            disks_data = fetch_disk_partitions(host_id)
            partitions = disks_data.get("results", [])
            

            # Initialize a list to hold disk information
            host["disks"] = []
            host_disks = []
            for partition in partitions:
                partition_name = partition.get("partitionName")
                if partition_name:
                    # Fetch measurements for each partition
                    disk_measurements = fetch_disk_measurements(host_id, partition_name)

                    # Extract relevant disk measurements
                    measurements = disk_measurements.get("measurements", [])
                    disk_info = {"partitionName": partition_name}
                    for measurement in measurements:
                        name = measurement.get("name")
                        data_points = measurement.get("dataPoints", [])
                        if data_points:
                            # Include all data points
                            values = []
                            for data_point in data_points:
                                timestamp = data_point.get("timestamp")
                                value = data_point.get("value")
                                if value is not None:
                                    # Convert bytes to human-readable format for specific measurements
                                    if name in ["DISK_PARTITION_SPACE_FREE", "DISK_PARTITION_SPACE_USED",
                                                "MAX_DISK_PARTITION_SPACE_FREE", "MAX_DISK_PARTITION_SPACE_USED"]:
                                        value = convert_bytes(value)
                                    values.append({"timestamp": timestamp, "value": value})
                            disk_info[name] = values

                    host_disks.append(disk_info)
                    # Add disk information to the host's disks list
                    host["disks"].append(disk_info)
            # Insert disk metrics into MySQL
            insert_disk_metrics(host_id,host_name, host_disks)
             
        # Output the updated hosts data
        print(json.dumps(hosts_data, indent=4))
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")

if __name__ == "__main__":
    main()
