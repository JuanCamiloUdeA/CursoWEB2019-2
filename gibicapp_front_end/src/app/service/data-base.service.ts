import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IDataBase } from '../model/DataBase';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class DataBaseService {

  constructor(
    private http:HttpClient,
  ) { }

  public getAllDataBase():Observable<IDataBase[]>{
    return this.http.get<IDataBase[]>('/assets/data/DataBase.json')
  }
}
