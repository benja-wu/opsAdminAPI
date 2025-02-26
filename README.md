# opsAdminAPI
Python tools to get MongoDB ops mms Administration API metrics and write into Mysql tables


# Prerequisites 
## MongoDB Ops mms 
1. Ops mms is already installed
2. Apply Admin API public key and private from Ops mms 

## Mysql tables 
1. create tables to hold hosts info and disks metrics 

``` mysql
CREATE TABLE hosts (
    host_id VARCHAR(255) PRIMARY KEY,
    host_name VARCHAR(255) NOT NULL,
    version VARCHAR(50) NOT NULL,
    ip_address VARCHAR(50) NOT NULL,
    replica_set_name VARCHAR(100),
    type_name VARCHAR(50) NOT NULL
);

CREATE TABLE disk_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    host_id VARCHAR(255),
    host_name VARCHAR(255) NOT NULL,
    partition_name VARCHAR(50),
    timestamp DATETIME,
    space_used VARCHAR(50),
    space_free VARCHAR(50),
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE CASCADE
);

```

## Python virutal env set up
Use Ptyhon virutal env

``` bash
python3 -m venv venv
source venv/bin/activate

# install packages
pip install requests
pip install mysql-connector-python

```

# Run the code 
```python
(venv) > python3 mmsAdminAPITool.py
```

## Example output
```json
{
    "links": [
        {
            "href": "https://hostname05.opsmanagerservers.org.net:8443/api/public/v1.0/groups/67b6fcd1536e9732f1ebf96d/hosts?pretty=true&pageNum=1&itemsPerPage=100",
            "rel": "self"
        }
    ],
    "results": [
        {
            "alertsEnabled": true,
            "authMechanismName": "SCRAM_SHA_1",
            "clusterId": "67b6ff00536e9732f1ec016f",
            "created": "2025-02-20T10:08:00Z",
            "groupId": "67b6fcd1536e9732f1ebf96d",
            "hasStartupWarnings": true,
            "hidden": false,
            "hiddenSecondary": false,
            "hostEnabled": true,
            "hostname": "hostname01.businessdbservers.org.internal",
            "id": "beface24079d327ff72049327cfc94fd",
            "ipAddress": "172.120.8.138",
            "journalingEnabled": true,
            "lastDataSizeBytes": 16574877,
            "lastIndexSizeBytes": 2531328,
            "lastPing": "2025-02-26T12:25:14Z",
            "lastRestart": "2025-02-22T00:36:15Z",
            "links": [
                {
                    "href": "https://hostname05.opsmanagerservers.org.net:8443/api/public/v1.0/groups/67b6fcd1536e9732f1ebf96d/hosts/beface24079d327ff72049327cfc94fd",
                    "rel": "self"
                }
            ],
            "logsEnabled": false,
            "lowUlimit": false,
            "port": 27017,
            "profilerEnabled": false,
            "replicaSetName": "app",
            "replicaStateName": "SECONDARY",
            "slaveDelaySec": 0,
            "sslEnabled": true,
            "systemInfo": {
                "memSizeMB": 7961,
                "numCores": 2
            },
            "typeName": "REPLICA_SECONDARY",
            "uptimeMsec": 388151,
            "username": "mms-automation",
            "version": "7.0.16",
            "disks": [
                {
                    "partitionName": "xvdb",
                    "DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 0.0
                        }
                    ],
                    "DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 1.0056490430507266
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 1.1879045659087664
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 1.3636997869150276
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 1.2584753842000094
                        }
                    ],
                    "DISK_PARTITION_IOPS_TOTAL": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 1.0056490430507266
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 1.1879045659087664
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 1.3636997869150276
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 1.2584753842000094
                        }
                    ],
                    "DISK_PARTITION_LATENCY_READ": [],
                    "DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 0.788335867243035
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 0.86685282171153
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 0.9596886880814383
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 0.8944030340902711
                        }
                    ],
                    "DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": "19.30 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": "19.28 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": "19.25 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": "19.25 GB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": "711.22 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": "725.72 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": "756.22 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": "758.26 MB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 96.52553551562517
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 96.45472771835732
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 96.30570760166052
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 96.29575826873355
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 3.474464484374828
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 3.545272281642694
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 3.6942923983394764
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 3.7042417312664533
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 0.0
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 48.98165470892745
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 61.5824175824176
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 71.89286910694096
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 66.9560565847991
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_TOTAL": [],
                    "MAX_DISK_PARTITION_LATENCY_READ": [],
                    "MAX_DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 4.000000000000001
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 5.846153846153845
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 4.809523809523808
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 5.333333333333332
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": "19.31 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": "19.29 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": "19.26 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": "19.26 GB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": "716.30 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": "729.67 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": "760.01 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": "763.16 MB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 96.6047181018786
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 96.48293498224419
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 96.3404397695815
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 96.33478489863214
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:37Z",
                            "value": 3.4992710368832434
                        },
                        {
                            "timestamp": "2025-02-25T11:58:37Z",
                            "value": 3.564570924617639
                        },
                        {
                            "timestamp": "2025-02-25T23:58:37Z",
                            "value": 3.7127996636337723
                        },
                        {
                            "timestamp": "2025-02-26T11:58:37Z",
                            "value": 3.7281756330402214
                        }
                    ]
                }
            ]
        },
        {
            "alertsEnabled": true,
            "authMechanismName": "SCRAM_SHA_1",
            "clusterId": "67b6ff00536e9732f1ec016f",
            "created": "2025-02-20T10:08:00Z",
            "groupId": "67b6fcd1536e9732f1ebf96d",
            "hasStartupWarnings": true,
            "hidden": false,
            "hostEnabled": true,
            "hostname": "hostname02.businessdbservers.org.internal",
            "id": "a28cd352081d58d677a34f43b23d6553",
            "ipAddress": "172.120.7.140",
            "journalingEnabled": true,
            "lastDataSizeBytes": 16574877,
            "lastIndexSizeBytes": 1781760,
            "lastPing": "2025-02-26T12:25:14Z",
            "lastRestart": "2025-02-22T00:34:58Z",
            "links": [
                {
                    "href": "https://hostname05.opsmanagerservers.org.net:8443/api/public/v1.0/groups/67b6fcd1536e9732f1ebf96d/hosts/a28cd352081d58d677a34f43b23d6553",
                    "rel": "self"
                }
            ],
            "logsEnabled": false,
            "lowUlimit": false,
            "port": 27017,
            "profilerEnabled": false,
            "replicaSetName": "app",
            "replicaStateName": "PRIMARY",
            "sslEnabled": true,
            "systemInfo": {
                "memSizeMB": 7961,
                "numCores": 2
            },
            "typeName": "REPLICA_PRIMARY",
            "uptimeMsec": 388285,
            "username": "mms-automation",
            "version": "7.0.16",
            "disks": [
                {
                    "partitionName": "xvdb",
                    "DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 0.0
                        }
                    ],
                    "DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 1.0064659249341303
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 1.173935069422123
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 1.3425284198555536
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 1.2438861751411157
                        }
                    ],
                    "DISK_PARTITION_IOPS_TOTAL": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 1.0064659249341303
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 1.173935069422123
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 1.3425284198555536
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 1.2438861751411157
                        }
                    ],
                    "DISK_PARTITION_LATENCY_READ": [],
                    "DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 0.7545844483473719
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 0.8007515832657782
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 0.8905292253912722
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 0.8767457654167463
                        }
                    ],
                    "DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": "19.29 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": "19.27 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": "19.24 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": "19.24 GB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": "719.06 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": "736.84 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": "768.81 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": "772.08 MB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 96.48726698082982
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 96.40041031155384
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 96.24421315313215
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 96.22821261602877
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 3.5127330191702013
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 3.599589688446157
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 3.7557868468678444
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 3.7717873839712444
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 0.0
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 52.08156480883754
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 60.63020313020313
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 72.2972027972028
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 67.79575529644623
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_TOTAL": [],
                    "MAX_DISK_PARTITION_LATENCY_READ": [],
                    "MAX_DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 4.560606060606061
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 5.692810457516339
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 4.999999999999999
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 5.6410256410256405
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": "19.30 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": "19.28 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": "19.25 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": "19.24 GB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": "722.73 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": "742.62 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": "775.18 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": "778.69 MB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 96.56698792856508
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 96.45289950486483
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 96.30962104095423
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 96.26981529019956
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:34Z",
                            "value": 3.530698680441444
                        },
                        {
                            "timestamp": "2025-02-25T11:58:34Z",
                            "value": 3.6278509709330726
                        },
                        {
                            "timestamp": "2025-02-25T23:58:34Z",
                            "value": 3.7869093236036475
                        },
                        {
                            "timestamp": "2025-02-26T11:58:34Z",
                            "value": 3.8040307579572357
                        }
                    ]
                }
            ]
        },
        {
            "alertsEnabled": true,
            "authMechanismName": "SCRAM_SHA_1",
            "clusterId": "67b6ff00536e9732f1ec016f",
            "created": "2025-02-20T10:08:00Z",
            "groupId": "67b6fcd1536e9732f1ebf96d",
            "hasStartupWarnings": true,
            "hidden": false,
            "hiddenSecondary": false,
            "hostEnabled": true,
            "hostname": "hostname03.businessdbservers.org.internal",
            "id": "0e694e40daf30f53d1e85d506e9d707d",
            "ipAddress": "172.120.0.178",
            "journalingEnabled": true,
            "lastDataSizeBytes": 16574877,
            "lastIndexSizeBytes": 1781760,
            "lastPing": "2025-02-26T12:25:14Z",
            "lastRestart": "2025-02-22T00:35:54Z",
            "links": [
                {
                    "href": "https://hostname05.opsmanagerservers.org.net:8443/api/public/v1.0/groups/67b6fcd1536e9732f1ebf96d/hosts/0e694e40daf30f53d1e85d506e9d707d",
                    "rel": "self"
                }
            ],
            "logsEnabled": false,
            "lowUlimit": false,
            "port": 27017,
            "profilerEnabled": false,
            "replicaSetName": "app",
            "replicaStateName": "SECONDARY",
            "slaveDelaySec": 0,
            "sslEnabled": true,
            "systemInfo": {
                "memSizeMB": 7961,
                "numCores": 2
            },
            "typeName": "REPLICA_SECONDARY",
            "uptimeMsec": 388212,
            "username": "mms-automation",
            "version": "7.0.16",
            "disks": [
                {
                    "partitionName": "xvdb",
                    "DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 0.0
                        }
                    ],
                    "DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 0.9917724029005187
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 1.1682217310971306
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 1.3357738063091855
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 1.2613606446300518
                        }
                    ],
                    "DISK_PARTITION_IOPS_TOTAL": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 0.9917724029005187
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 1.1682217310971306
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 1.3357738063091855
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 1.2613606446300518
                        }
                    ],
                    "DISK_PARTITION_LATENCY_READ": [],
                    "DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 0.7354681847479824
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 0.7472706099828339
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 0.8590252070555835
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 0.8816879899696192
                        }
                    ],
                    "DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": "19.29 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": "19.28 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": "19.24 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": "19.24 GB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": "712.59 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": "726.03 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": "765.01 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": "764.45 MB"
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 96.51883910777615
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 96.45321560199136
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 96.26275235337332
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 96.2654936413078
                        }
                    ],
                    "DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 3.4811608922238535
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 3.5467843980086102
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 3.7372476466266535
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 3.734506358692206
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_READ": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 0.0
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 0.0
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 50.1596585232949
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 62.036806673034214
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 71.45754245754244
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 69.56443556443557
                        }
                    ],
                    "MAX_DISK_PARTITION_IOPS_TOTAL": [],
                    "MAX_DISK_PARTITION_LATENCY_READ": [],
                    "MAX_DISK_PARTITION_LATENCY_WRITE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 4.000000000000001
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 10.333333333333337
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 4.222222222222222
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 3.999999999999999
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": "19.32 GB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": "19.29 GB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": "19.26 GB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": "19.26 GB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": "718.40 MB"
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": "733.34 MB"
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": "771.43 MB"
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": "770.65 MB"
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_FREE": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 96.62705886108274
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 96.50185961925987
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 96.35882764156895
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 96.32634295967834
                        }
                    ],
                    "MAX_DISK_PARTITION_SPACE_PERCENT_USED": [
                        {
                            "timestamp": "2025-02-24T23:58:32Z",
                            "value": 3.5095271766887244
                        },
                        {
                            "timestamp": "2025-02-25T11:58:32Z",
                            "value": 3.582518179551376
                        },
                        {
                            "timestamp": "2025-02-25T23:58:32Z",
                            "value": 3.768578700028497
                        },
                        {
                            "timestamp": "2025-02-26T11:58:32Z",
                            "value": 3.7647774299162
                        }
                    ]
                }
            ]
        }
    ],
    "totalCount": 3
}
```
