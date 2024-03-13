cd ./cloud-functions

gcloud functions deploy call_model \
    --runtime python311 \
    --trigger-http \
    --entry-point=call_model \
    --source=.

