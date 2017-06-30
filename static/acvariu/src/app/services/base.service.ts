import { Injectable, Inject } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import { Observable, Subject } from 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';
import { ExecutionElement } from '../models/execution-element.model';

@Injectable()
export class BaseService<T> {
    protected apiUrl: string = "";
    protected _http: Http;
    protected originUrl: string;
    constructor(_http: Http, @Inject('ORIGIN_URL') originUrl: string) {
        this._http = _http;
        this.originUrl = originUrl;
        //this.apiUrl = originUrl + '/automation/';
        this.apiUrl = 'http://192.168.1.200' + '/automation/';
    }
    protected RegenerateData = new Subject<number>();
    // Observable string streams
    RegenerateData$ = this.RegenerateData.asObservable();

    protected AnnounceChange(mission: number) {

        this.RegenerateData.next(mission);
    }

    public LoadData(): Promise<T[]> {
        return this._http.get(this.apiUrl + "status/")
            .toPromise()
            .then(response => this.extractArray(response))
            .catch(this.handleErrorPromise);
    }

    public Add(model) {
        let headers = new Headers({
            'Content-Type':
            'application/json; charset=utf-8'
        });
        let options = new RequestOptions({ headers: headers });
        delete model["id"];
        let body = JSON.stringify(model);
        return this._http.post(this.apiUrl, body,
            options).toPromise().catch(this.handleErrorPromise);
    }
    public Update(model) {
        let headers = new Headers({
            'Content-Type':
            'application/json; charset=utf-8'
        });
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify(model);
        return this._http.put(this.apiUrl, body,
            options).toPromise().catch(this.handleErrorPromise);
    }
    public Delete(id: number) {
        return this._http.delete(this.apiUrl + '?id=' +
            id).toPromise().catch(this.handleErrorPromise);
    }

    protected extractArray(res: Response, showprogress: boolean = true) {
        let data = res.json();

        return data || [];
    }

    protected handleErrorPromise(error: any): Promise<void> {
        try {
            error = JSON.parse(error._body);
        } catch (e) {
        }

        let errMsg = error.errorMessage
            ? error.errorMessage
            : error.message
                ? error.message
                : error._body
                    ? error._body
                    : error.status
                        ? `${error.status} - ${error.statusText}`
                        : 'unknown server error';

        console.error(errMsg);
        return Promise.reject(errMsg);
    }
} 