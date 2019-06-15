import { Component, OnInit } from '@angular/core';
import { PopoverController } from '@ionic/angular';

@Component({
  selector: 'app-popinfo1',
  templateUrl: './popinfo1.component.html',
  styleUrls: ['./popinfo1.component.scss'],
})
export class Popinfo1Component implements OnInit {

  constructor(private popoverCtrl: PopoverController) { }

  ngOnInit() {}

  onClick(){
    this.popoverCtrl.dismiss();

  }
}
