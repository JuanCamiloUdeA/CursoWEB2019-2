import { Component, OnInit } from '@angular/core';
import { DataBaseService } from '../service/data-base.service';
import { IDataBase } from '../model/DataBase';

@Component({
  selector: 'app-data-base-info',
  templateUrl: './data-base-info.component.html',
  styleUrls: ['./data-base-info.component.css']
})
export class DataBaseInfoComponent implements OnInit {

  public DataBase: IDataBase[];

  constructor(
    private DataBaseService:DataBaseService,
  ) { }

  ngOnInit(): void {
    this.DataBaseService.getAllDataBase().subscribe((DataBase:IDataBase[]) => {
        this.DataBase = DataBase; 
    });
  }

}
