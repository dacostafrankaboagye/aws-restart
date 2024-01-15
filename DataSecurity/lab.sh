
cd ~ 

aws configure 

vi ~/.aws/credentials 

pip3 install aws-encryption-sdk-cli 

export PATH=$PATH:/home/ssm-user/.local/bin 

keyArn=arn:aws:kms:us-west-2:851725433745:key/dba6ce38-ecfd-4f4a-88f6-a5f41d04d5e4


aws-encryption-cli --encrypt \ 

                     --input secret1.txt \ 

                     --wrapping-keys key=$keyArn \ 

                     --metadata-output ~/metadata \ 

                     --encryption-context purpose=test \ 

                     --commitment-policy require-encrypt-require-decrypt \ 

                     --output ~/output/. 

 aws-encryption-cli --decrypt \ 

                     --input secret1.txt.encrypted \ 

                     --wrapping-keys key=$keyArn \ 

                     --commitment-policy require-encrypt-require-decrypt \ 

                     --encryption-context purpose=test \ 

                     --metadata-output ~/metadata \ 

                     --max-encrypted-data-keys 1 \ 

                     --buffer \ 

                     --output . 
