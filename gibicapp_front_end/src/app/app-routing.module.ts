import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent} from "./home/home.component";
import { HeaderComponent} from "./header/header.component";
import { LoginComponent} from "./login/login.component";
import { Header2Component} from "./header2/header2.component";
import { DataBaseInfoComponent } from './data-base-info/data-base-info.component';
import { SolicitudComponent } from './solicitud/solicitud.component';
import {ReviewComponent} from './review/review.component';


const routes: Routes = [
  {path: "home", component:HomeComponent},
  {path: "header", component:HeaderComponent},
  {path: "header2", component:Header2Component},
  {path: "login", component:LoginComponent},
  {path: "data-base-info", component:DataBaseInfoComponent},
  {path: "solicitud", component:SolicitudComponent},
  {path: "review",component:ReviewComponent},
  {path: "**", redirectTo: "/home"},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: [],
})
export class AppRoutingModule { }
