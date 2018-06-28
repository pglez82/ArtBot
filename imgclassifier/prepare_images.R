ORIGINAL_IMAGES_PATH <- "images/"
IMAGES_PATH <- "images_aug/"

#Generates new images in order to have more data to train the CNN
dataAugmentation<-function()
{
  library(EBImage)

  dimx<-224
  dimy<-224
  
  #brightness, constrast, rotation
  brightness=seq(-0.4,0.4,by=0.2)
  contrast=c(0.8,1.2)
  rotation=seq(-6,6,by=2)

  images <- list.files(path=ORIGINAL_IMAGES_PATH,recursive = TRUE)

  pb=txtProgressBar(min = 0, max = length(brightness)*length(contrast)*length(rotation)*length(images), initial = 0,style=3)
  
  unlink(IMAGES_PATH, recursive=TRUE)
  dir.create(IMAGES_PATH)
  
  step=0
  for (image in images)
  {
    pic <- readImage(paste0(ORIGINAL_IMAGES_PATH,image))
    
    originalDim<-dim(pic)
    if(originalDim[1]>originalDim[2])
    {
      pic<-translate(
        resize(pic,w=224,output.dim=c(224,224)),
        c(0,(224-round(224*dim(pic)[2]/dim(pic)[1]))%/%2))
    }
    else
    {
      pic<-translate(
        resize(pic,h=224,output.dim=c(224,224)),
        c((224-round(224*dim(pic)[1]/dim(pic)[2]))%/%2,0))
    }
    
    dir.create(paste0(IMAGES_PATH,dirname(image)))
    #We change the brightness of the image
    for (b in brightness)
    {
      picb<-pic+b
      #Change the contrast
      for (c in contrast)
      {
        picc<-picb*c
        for (r in rotation)
        {
          picr <- rotate(picc,r,output.dim = c(dimx,dimy),bg.col=picc[1][1][1])
          writeImage(picr,paste0(IMAGES_PATH,dirname(image),"/","b",b,"c",c,"r",r,".jpg"))
		      step=step+1
		      setTxtProgressBar(pb,step)
        }   
      }
    }
  }
}

dataAugmentation()

