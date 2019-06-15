import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { UiServiceService } from '../../services/ui-service.service';

@Component({
  selector: 'app-info-obra',
  templateUrl: './info-obra.page.html',
  styleUrls: ['./info-obra.page.scss'],
})
export class InfoObraPage implements OnInit {
  //Quitar
  code: number;

  title: string;
  clasificator: string;
  image: any;
  description: string;


  constructor(public router: Router, public uiService: UiServiceService, public activatedRoute: ActivatedRoute  ) { }

  ngOnInit() {
    const formDataToUpload = this.uiService.getFormaData();
    this.uiService.post(formDataToUpload).subscribe(
      data => {
        this.code = data.code;
        this.title = data.name;
        this.clasificator = data.probability;
        this.description = data.desciption;
      });
      this. artworkInformation();
  }

/**
 * Método para mostrar la información de la obra de arte en función del código que recibamos del servidor.
 */
  artworkInformation() {
    this.image =  this.uiService.getImagen();


  }
/**
 * Método para volver a la página de la cámara.
 */
  exit() {
    this.router.navigateByUrl('/tabs/art');
  }
}
