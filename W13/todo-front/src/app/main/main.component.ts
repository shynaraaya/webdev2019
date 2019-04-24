import { Component, OnInit } from '@angular/core';
import { ProviderService } from './services/provider.service';
import { ITaskList } from './models/todo';
import {ITask} from './models/todo';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public tasklist: ITaskList[]=[];
  public loading = false;
   
  public lists: ITask[]=[]; 

  public name: any='';

  public logged = false;
  public login: any ='';
  public password: any ='';


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged = true;
    }
    if(this.logged){
    this.provider.getTaskList().then(res =>{
      this.tasklist = res;
      setTimeout( () => {
        this.loading=true;
      }, 2000);
    });
    }
  }

  getTasks(task: ITaskList){
    this.provider.getTasks(task).then(res =>{
      this.lists = res;
    });

  }

  updateTaskList(c: ITaskList){
    this.provider.updateTaskList(c).then(res =>{
      console.log(c.name+'updated');
    });
  }

  deleteTaskList(c: ITaskList){
    this.provider.deleteTaskList(c.id).then(res => {
      console.log(c.name + 'deleted');
      this.provider.getTaskList().then( res => {
        this.tasklist = res;
      })
    })
  }

  createTaskList(){
    if(this.name !== '') {
    this.provider.createTaskList(this.name).then( res => {
      this.name = '';
      this.tasklist.push(res);
      })
    }
  }

  auth() {
    console.log(this.login + " " + this.password);

    if (this.login !== '' && this.password !== '') {
      
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);

        console.log(res);

        this.logged = true;

        this.provider.getTaskList().then(r => {
          this.tasklist = r;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });

      });
    }
  }

  logout(){
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged=false;
    })
  }

}
