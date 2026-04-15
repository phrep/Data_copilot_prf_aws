from unittest.mock import patch, MagicMock


@patch("boto3.client")
def test_athena_connection(mock_boto_client):
    
    import boto3
    mock_client_instance = MagicMock()
    mock_client_instance.list_databases.return_value = {
        "DatabaseList": ["db1", "db2"]
    }

    mock_boto_client.return_value = mock_client_instance

    
    client = boto3.client("athena")

    response = client.list_databases(CatalogName="AwsDataCatalog")

    assert "DatabaseList" in response