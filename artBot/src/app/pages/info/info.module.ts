import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { Popinfo1Component } from '../../components/popinfo1/popinfo1.component';

import { IonicModule } from '@ionic/angular';
import { ComponentsModule } from '../../components/components.module';
import { InfoPage } from './info.page';
import { ModalInfoPage } from '../modal-info/modal-info.page';
import { ModalInfoPageModule } from '../modal-info/modal-info.module';

const routes: Routes = [
  {

    path: '',
    component: InfoPage
  }
];

@NgModule({
  entryComponents: [Popinfo1Component, ModalInfoPage ],
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ComponentsModule,ModalInfoPageModule,
    RouterModule.forChild(routes)
  ],
  declarations: [InfoPage]
})
export class InfoPageModule {}
