import { Component, OnInit, Input } from '@angular/core';
import { ModalController, NavController } from '@ionic/angular';


declare var google;

@Component({
  selector: 'app-modal-info',
  templateUrl: './modal-info.page.html',
  styleUrls: ['./modal-info.page.scss'],
})
export class ModalInfoPage implements OnInit {

  @Input() titulo:string;


  constructor(public modalCtrl: ModalController, public navCtrl: NavController ) {}

  ngOnInit() {  }

  
  exit() {
    this.modalCtrl.dismiss();
  }
}
