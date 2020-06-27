import { Component, OnInit } from '@angular/core';
import { DataBaseService } from '../service/data-base.service';
import { IDataBase } from '../model/DataBase';
import {MatDialog} from '@angular/material/dialog';
import { DialogoComponent } from '../dialogo/dialogo.component';

@Component({
  selector: 'app-solicitud',
  templateUrl: './solicitud.component.html',
  styleUrls: ['./solicitud.component.css']
})
export class SolicitudComponent implements OnInit {

  public DataBase: IDataBase[];
  constructor(private DataBaseService:DataBaseService,
              private dialog: MatDialog) { }

  ngOnInit(): void {
    this.DataBaseService.getAllDataBase().subscribe((DataBase:IDataBase[]) => {
        this.DataBase = DataBase; 
    });
  }
  openDialog() {
    this.dialog.open(DialogoComponent)
  }
}


