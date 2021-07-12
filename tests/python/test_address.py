import os

from smartredis import Client


def test_address(use_cluster):
    # get env var to set through client init
    ssdb = os.environ["SSDB"]
    del os.environ["SSDB"]

    # client init should fail if SSDB not set
    c = Client(address=ssdb, cluster=use_cluster)

    # check if SSDB was set anyway
    assert os.environ["SSDB"] == ssdb


def test_dbnode_info_command(use_cluster):
    # get env var to set through client init
    # if cluster, only test first DB
    ssdb = os.environ["SSDB"]
    if use_cluster:
        db_info_addr = ssdb.split(",")
    else:
        db_info_addr = [ssdb]
    del os.environ["SSDB"]

    # client init should fail if SSDB not set
    client = Client(address=ssdb, cluster=use_cluster)

    info = client.get_db_node_info(db_info_addr)

    assert len(info) > 0
