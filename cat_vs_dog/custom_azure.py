
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'catsvsdogs2' # Must be replaced by your <storage_account_name>
    account_key = 'tYeYYsz4+9UMNVicOoNP8NSrB11TvDO1zUDdEBTSOhqxpqtxlE8724gcGOPAOT9tNEXMeU8fQRrcFKvnaF/efg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'catsvsdogs2' # Must be replaced by your storage_account_name
    account_key = 'tYeYYsz4+9UMNVicOoNP8NSrB11TvDO1zUDdEBTSOhqxpqtxlE8724gcGOPAOT9tNEXMeU8fQRrcFKvnaF/efg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
