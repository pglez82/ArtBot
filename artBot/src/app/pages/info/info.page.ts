import { Component, OnInit } from '@angular/core';
import { ModalController, NavController,LoadingController } from '@ionic/angular';
import { ModalInfoPage } from '../modal-info/modal-info.page';


import { PopoverController } from '@ionic/angular';
import { Popinfo1Component } from '../../components/popinfo1/popinfo1.component';

@Component({
  selector: 'app-info',
  templateUrl: './info.page.html',
  styleUrls: ['./info.page.scss'],
})
export class InfoPage implements OnInit {
isLoaded: boolean;
open: boolean;
select = 'info museum';
today: any;

  constructor(public modalCtrl: ModalController, public popoverCtrl: PopoverController ) { }

  ngOnInit() {
    this.open = this.isValidDate();
    this.segment();
  }

  segment() {
    setTimeout(() => {
      this.isLoaded = true;
    }, 2000);
  }

/**
 * Método asíncrono para mostrar popover.
 * @param evento 
 */
  async mostrarPop( evento: any ) {

    const popover = await this.popoverCtrl.create({
      component: Popinfo1Component,
      event: evento,
      mode: 'ios',
      backdropDismiss: false
    });

    await popover.present();
    const { data } = await popover.onWillDismiss();

  }
/**
 * Método asíncrono para mostrar la información del escultor o del museo.
 */
  async mostrarInfo(id?: number) {
    let modal: any;
    switch (id) {
      case 1:
         modal = await this.modalCtrl.create({
        component: ModalInfoPage,
        componentProps: {
          titulo: 'THE BUILDING'
        }});
        break;
      case 2:
        modal = await this.modalCtrl.create({
          component: ModalInfoPage,
          componentProps: {
            titulo: 'SCULPTURAL PARK'
          }
        });
        break;
        case 3:
            modal = await this.modalCtrl.create({
              component: ModalInfoPage,
              componentProps: {
                titulo: 'Period 1918 - 1928'
              }
            });
        break;
        case 4:
            modal = await this.modalCtrl.create({
              component: ModalInfoPage,
              componentProps: {
                titulo: 'Period 1928 - 1937'
              }
            });
        break;
      default:
    }
    await modal.present();

  }
/**
 * Método para comprobar si el museo está abierto en la hora en que se consulta.
 */
isValidDate() {

const today = new Date(),
 month = today.getMonth(),
 day = today.getDay(),
 hour = today.getHours();

    switch (month) {
      case 0:
      case 1:
      case 2:
      case 3:
      case 4:
      case 9:
      case 10:
      case 11:
              switch (day) {
                case 2:
                case 3:
                case 4:
                case 5:
                  if (hour >= 17 && hour <= 19) {
                    this.open = true;
                  }
                  break;
                case 6:
                case 0:
                  if (hour >= 12 && hour <= 14 || hour >= 17 && hour <= 19) {
                    this.open = true;
                  }
                  break; 
                case 1: 
                default:
                this.open = false;
              }
      break;
      case 5:
      case 6:
      case 7:
      case 8:
        if (day !== 1) {
          if (hour >= 12 && hour <= 14 || hour >= 18 && hour <= 21) {
            this.open = true;
          }
        }
    }
    const intervalo = setInterval(this.isValidDate, 1000);
    return (this.open);

}

}