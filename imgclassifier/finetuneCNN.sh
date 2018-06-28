nclasses=`wc -l < labels.txt`
nexamples=`wc -l < artbot_train.lst`

#Parameters
model=resnet-18
finetuned_model=resnet-18-ft
batch_size=32
epochs=10

mkdir -p models/finetuned/$finetuned_model

python ~/incubator-mxnet/example/image-classification/fine-tune.py --pretrained-model models/$model/$model --data-train artbot_train.rec --data-val artbot_val.rec --load-epoch 0 --random-crop 0 --random-mirror 0 --num-epochs $epochs --rgb-mean 0,0,0 --num-classes $nclasses --model-prefix models/finetuned/$finetuned_model/$finetuned_model --batch-size $batch_size --num-examples $nexamples --layer-before-fullc 'flatten0'
