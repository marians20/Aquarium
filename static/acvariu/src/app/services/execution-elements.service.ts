import { Injectable, Inject } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import { Observable, Subject } from 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';
import { BaseService } from './base.service';
import { ExecutionElement } from '../models/execution-element.model';

@Injectable()
export class ExecutionElementsService extends BaseService<ExecutionElement> {
    constructor(_http: Http, @Inject('ORIGIN_URL') originUrl: string) {
        super(_http, originUrl);
    }

    public Stop(id: number) {
        let url = this.apiUrl + "set/" + id + "/0/"
        console.log(url);
        return this._http.get(url)
            .toPromise()
            .then(response => this.extractArray(response))
            .catch(this.handleErrorPromise);     
    }

    public Start(id: number) {
        let url = this.apiUrl + "set/" + id + "/1/";
        console.log(url);
        return this._http.get(url)
            .toPromise()
            .then(response => this.extractArray(response))
            .catch(this.handleErrorPromise);        
    }

    public Automatic(id: number) {
        let url = this.apiUrl + "setauto/" + id + "/"
        console.log(url);
        return this._http.get(url)
            .toPromise()
            .then(response => this.extractArray(response))
            .catch(this.handleErrorPromise);
    }

    protected extractArray(res: Response, showprogress: boolean = true) {
        let data = res.json().ExecutionElements;

        return data || [];
    }
} 