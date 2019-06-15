import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { ArtPage } from './art.page';
import { PipesModule } from '../../pipes/pipes.module';

const routes: Routes = [
  {
    path: '',
    component: ArtPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule, PipesModule,
    RouterModule.forChild(routes)
  ],
  declarations: [ArtPage]
})
export class ArtPageModule {}
