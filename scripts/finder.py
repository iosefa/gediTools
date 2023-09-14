from gedi_tools.handlers.cmr import GediAgent

if __name__ == "__main__":
    bbox = [46.78027, -16.34996, 46.84995, -16.31315]
    product = 'GEDI02_B.002'
    download_path = '/Users/iosefa/gedi'
    start_date = '2022-06-01'
    end_date = '2023-06-01'

    files = GediAgent._get_download_links(product, start_date, end_date, bbox, None)

    print(files)

    # GediAgent.download_gedi()
    # print(f"Sentinel found {len(sentinel.download_links)} {sentinel.product} files for download.")
    # sentinel.download_gedi()

    # controller.l2b_2_poly(
    #     "/Users/iosefa/gedi/",
    #     "/Users/iosefa/fire-history/l2b_test.gpkg",
    #     clean=False,
    #     bbox=[46.78027, -16.34996, 46.84995, -16.31315])
