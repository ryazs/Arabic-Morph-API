# Region Indo
gcloud builds submit --tag asia-southeast2-docker.pkg.dev/capstone-project-arabic-morph/api-arabic

gcloud run deploy backend-mlgc \
--image asia-southeast2-docker.pkg.dev/capstone-project-arabic-morph/api-arabic \
--platform managed \
--region asia-southeast2 \
--allow-unauthenticated \
--memory 1Gi \
--cpu 1

# Multi Region Asia
gcloud builds submit --tag asia-docker.pkg.dev/capstone-project-arabic-morph/arabic-api

gcloud run deploy backend-mlgc \
--image asia-docker.pkg.dev/capstone-project-arabic-morph/arabic-api \
--platform managed \
--region asia-southeast1 \
--allow-unauthenticated \
--memory 1Gi \
--cpu 1

# Using GCR
gcloud builds submit --tag gcr.io/capstone-project-arabic-morph/arabic-api-repo

gcloud run deploy backend-mlgc \
--image gcr.io/capstone-project-arabic-morph/arabic-api-repo \
--platform managed \
--region asia-southeast2 \
--allow-unauthenticated \
--memory 1Gi \
--cpu 1