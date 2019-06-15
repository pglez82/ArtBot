import { Component, OnInit } from '@angular/core';
import { Camera, CameraOptions } from '@ionic-native/camera/ngx';
import { Router } from '@angular/router';
import { UiServiceService } from '../../services/ui-service.service';
import { HttpClient } from '@angular/common/http';
import { LoadingController } from '@ionic/angular';


@Component({
  selector: 'app-art',
  templateUrl: './art.page.html',
  styleUrls: ['./art.page.scss'],
})
export class ArtPage implements OnInit {

 buttonDisabledClear = true;
 buttonDisabledCamara = false;
 buttonDisabledPicture = false;
 buttonDisabledSend = true;

 photos: any[];
 image: string = null;

  slideOpts = {
    slidesPerView: 2.5,
    freeMode: true
  };

constructor(public camera: Camera, public router: Router, public loadingController: LoadingController,
            public uiService: UiServiceService, public http: HttpClient) { }

ngOnInit() {

  this.uiService.onLoadPhotos().subscribe(
    data => {
      this.photos = data['photos'];

    }
  );

}

/**
 * Método para limpiar la previsualización de la foto.
 */
clear(num?: number) {
  if (num === 1) {
    this.uiService.alertInfo('Deleting Preview...');
  }

  this.image = null;
  this.inactiveButtons(2);
}

/**
 * Método que abre la cámara y toma una foto para enviarla al servidor.
 */
camara() {
  const options: CameraOptions = {
    quality: 70,
    destinationType: this.camera.DestinationType.DATA_URL,
    encodingType: this.camera.EncodingType.JPEG,
    mediaType: this.camera.MediaType.PICTURE,
    targetWidth: 300,
    targetHeight: 700
  }

  this.camera.getPicture(options).then((imageData) => {
    this.image = 'data:image/jpeg;base64,' + imageData;
    this.inactiveButtons(1);
  }, (err) => {
    console.log('ERROR ' + err);
  });

    
  
}
/**
 * Método que abre la galería de imágenes del móvil y la envía al servidor.
 */
libreria() {
  const options: CameraOptions = {
    quality: 70,
    targetWidth: 300,
    targetHeight: 700,
    destinationType: this.camera.DestinationType.DATA_URL,
    sourceType: this.camera.PictureSourceType.PHOTOLIBRARY,
    saveToPhotoAlbum: false
}

  this.camera.getPicture(options).then((imageData) => {

  this.image = 'data:image/jpeg;base64,' + imageData;
  this.inactiveButtons(1);
  }, (err) => {
    console.log('ERROR ' + err);
  });

}

/**
 * Método para enviar una imagen en Base64 a un web service.
 */
  sendPicture( ) {
        const random = Math.floor(Math.random() * 100);
        const fileName = 'myImage_' + random + '.jpg';

        const formDataToUpload = new FormData();
        const blob = this.dataURItoBlob(this.image);

        formDataToUpload.append('image', blob, fileName);

        this.uiService.setImagen(this.image);
        this.uiService.setFormaData(formDataToUpload);

        this.clear();
        this.router.navigateByUrl('/info-obra');

  }

  /**
   * Método privado que permite decodificar una imgen en BASE64 en un Blob para poder enviarla a través de un formData al servidor.
   */
private dataURItoBlob(dataURI: any) {

  // convert base64/URLEncoded data component to raw binary data held in a string
              let byteString: string;
              if (dataURI.split(',')[0].indexOf('base64') >= 0) {
                  byteString = atob(dataURI.split(',')[1]);

              } else {
                  byteString = unescape(dataURI.split(',')[1]);
              }
              // separate out the mime component
              const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
              // write the bytes of the string to a typed array

              const ia = new Uint8Array(byteString.length);
              for (let i = 0; i < byteString.length; i++) {
                  ia[i] = byteString.charCodeAt(i);
              }
              return new Blob([ia], {type: mimeString});
          }

  /**
   * Método privado que habilita y deshabilita botones para que el usuario interactúe con la aplicación malintencionadamente.
   * @param button
   */
private inactiveButtons(button: number) {

  switch (button) {
    case 1:
      // Camara y galería
      this.buttonDisabledClear = false;
      this.buttonDisabledCamara = true;
      this.buttonDisabledPicture = true;
      this.buttonDisabledSend = false;
      break;
    case 2:
      this.buttonDisabledClear = true;
      this.buttonDisabledCamara = false;
      this.buttonDisabledPicture = false;
      this.buttonDisabledSend = true;
      break;

    default:
      this.buttonDisabledClear = true;
      this.buttonDisabledCamara = false;
      this.buttonDisabledPicture = false;
      this.buttonDisabledSend = true;
  }
}

}