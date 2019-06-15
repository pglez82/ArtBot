import { Injectable } from '@angular/core';
import { AlertController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class UiServiceService {

  imagen: string;
  formDataToUpload: FormData;
  photos: any[];

  constructor(public alertController: AlertController, public http: HttpClient) { }

/**
 * Método asíncrono que muestra un alert pasándole un mensaje.
 */
async alertInfo( message: string ) {
const alert = await this.alertController.create({
message,
buttons: ['OK']
});

await alert.present();
}

// Métodos para pasar la imagen tomada por la cámara o seleccionada de la galería de un componente a otro.
setImagen(imagen: string) {
  this.imagen = imagen;
}
getImagen(): string {
  return this.imagen;
}
setFormaData(formDataToUpload: FormData) {
    this.formDataToUpload = formDataToUpload;
}
getFormaData(): FormData {
  return this.formDataToUpload;
}

post(formDataToUpload: FormData): Observable<any> {
  return this.http.post('http://192.168.11.1:5000/upload', formDataToUpload);
}

onLoadPhotos(): Observable<any> {
  return this.http.get('http://192.168.11.1:5000/photos');
}

}
