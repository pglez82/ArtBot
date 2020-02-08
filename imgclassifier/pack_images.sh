python ~/incubator-mxnet/tools/im2rec.py artbot images_aug --list TRUE --recursive TRUE --train-ratio .8 --exts .jpg > labels.txt
python ~/incubator-mxnet/tools/im2rec.py artbot_train.lst images_aug --pass-through TRUE --num-thread 2
python ~/incubator-mxnet/tools/im2rec.py artbot_val.lst images_aug --pass-through TRUE --num-thread 2


