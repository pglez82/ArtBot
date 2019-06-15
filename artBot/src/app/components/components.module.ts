import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { Popinfo1Component } from './popinfo1/popinfo1.component';
import { IonicModule } from '@ionic/angular';

@NgModule({
  declarations: [
    HeaderComponent,Popinfo1Component
  ],
  exports:[
    HeaderComponent,Popinfo1Component
  ],
  imports: [
    CommonModule, IonicModule
  ]
})
export class ComponentsModule { }
