from pdf_spliter import FS,SS,con

if con.splitting_type == 'full'.lower():
    FS.full_split_proses(con.pdf_path,con.page_len,con.chapter_name)
    print("Your PDF Splitting Successfully.")
else:
    SS.specific_split_proses(con.pdf_path,con.list_of_page,con.chapter_name)
    print("Your PDF Splitting Successfully.")
