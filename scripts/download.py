from gediTools import controller

# sentinel = controller.SentinelDroid(
#     product='GEDI02_B.002',
#     download_path = '/media/iosefa/data/gedi_2b',
#     bbox = [46.78027, -16.34996, 46.84995, -16.31315]
# )
sentinel = controller.FinderDroid(
    product='GEDI02_B.002',
    download_path='/Users/iosefa/gedi',
    start_date='2022-06-01',
    bbox=[46.78027, -16.34996, 46.84995, -16.31315]
)

print(f"Sentinel found {len(sentinel.download_links)} {sentinel.product} files for download.")
# sentinel.download_gedi(batch_size=1)
