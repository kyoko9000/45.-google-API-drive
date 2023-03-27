import io

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from google_api_lib import service

service = service()

'''  1..............for upload file to google drive................
source code: https://developers.google.com/drive/api/v3/manage-uploads
'''
folder_id = ["1ZfpiRFSqwF0M7jhLWjUv8rUoPRZsOUCR"]
file_names = ["1.jpeg", "2.jpeg"]
for file_name in file_names:
    file_metadata = {
        "name": file_name,
        "parents": folder_id
    }
    media = MediaFileUpload("icons/{0}".format(file_name), resumable=True)
    send = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, name"
    ).execute()
    print(' File ID: %s' % send.get('id'), "\n", 'File name: %s' % send.get('name'))


'''  2................download files on google drive ....................
source code: https://developers.google.com/drive/api/v3/manage-downloads
'''
# file_id = '1cGgis3jIsgUqGrW_U_QndlDesbgeo_-5'
# request = service.files().get_media(fileId=file_id)
# fh = io.BytesIO()
# downloader = MediaIoBaseDownload(fh, request)
# done = False
# while done is False:
#     status, done = downloader.next_chunk()
#     print("Download %d%%." % int(status.progress() * 100))
#     with open("C:/Users/DELL/Desktop/New folder/1.jpeg", "wb") as f:
#         f.write(fh.getvalue())

"""  3.............get link google drive............
source code: https://learndataanalysis.org/source-code-generate-file-sharing-url-with-google-drive-api-in-python/
"""
# Sharing file Permission
# file_id = '1ZfpiRFSqwF0M7jhLWjUv8rUoPRZsOUCR'
#
# request_body = {
#     'role': 'reader',
#     'type': 'anyone'
# }
#
# response_permission = service.permissions().create(
#     fileId=file_id,
#     body=request_body
# ).execute()
#
# print(response_permission)
#
# # Print Sharing URL
# response_share_link = service.files().get(fileId=file_id,
#                                           fields='webViewLink').execute()
#
# print(response_share_link['webViewLink'])
#
# # Remove Sharing file Permission
# # service.permissions().delete(fileId=file_id,
# #                              permissionId='anyoneWithLink').execute()
# print("complete")