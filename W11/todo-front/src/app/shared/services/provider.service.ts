import { Injectable } from '@angular/core';
import { MainService } from './main.service'
import { HttpClient } from '@angular/common/http'
import { ITaskList, ITask } from '../models/models'

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) { 
  	super(http)
  }

  getTaskLists(): Promise<ITaskList[]>{
  	return this.get('http://127.0.0.1:8000/api/task_lists/', {})
  }

  getTasks(task_list: ITaskList): Promise<ITask[]>{
  	return this.get(`http://127.0.0.1:8000/api/task_lists/${task_list.id}/tasks`, {})
  }
}
