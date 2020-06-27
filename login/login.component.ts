import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { MatDialog} from "@angular/material/dialog";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router) { }

username:string;
password:string;

  ngOnInit(): void {
  }

login():void{

  if(this.username== 'admin' && this.password =='1234'){
      window.open("http://localhost:4200/review","_self");
  } else {
      alert("Datos invalidos, Los datos correctos son: \nUsuario: admin \nContraseña:1234");
  }

  }


}


