import { Component, Inject, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Subscription } from 'rxjs/Subscription';
import { ExecutionElement } from '../../models/execution-element.model';
import { ExecutionElementsService } from '../../services/execution-elements.service';

@Component({
  selector: 'app-execution-elements',
  providers: [ExecutionElementsService],
  templateUrl: './execution-elements.component.html',
  styleUrls: ['./execution-elements.component.css']
})
export class ExecutionElementsComponent implements OnInit {
    public executionElements: ExecutionElement[] = [];
    subscription: Subscription;

    Refresh() {
        this._service.LoadData().then(data => {
            console.log(data);
            this.executionElements = data;
        })
    }

    constructor(http: Http, @Inject('ORIGIN_URL') originUrl: string,
      private _service: ExecutionElementsService) {
        //super();
        this.subscription = _service.RegenerateData$.subscribe(
            mission => {
                console.log("Good !! ", mission);
                this.Refresh();
            });
    }

    ngOnInit() {
        this.Refresh();
    }
    onUpdate(elem) {
        console.log(elem);
        this._service.Update(elem).then(data => {
        })
    }
    onDelete(elem: number) {
        console.log("Delete Form ! ");
        console.log(elem);
        this._service.Delete(elem).then(data => {
            this.Refresh();
        })
    }
    onCreate() {
        console.log('Create invoked.');
    }
    ngOnDestroy() {
        // prevent memory leak when component destroyed
        this.subscription.unsubscribe();
    }

    onStop(element_id: number) {
        this._service.Stop(element_id).then(data => {
            console.log(data);
            this.executionElements = data;
        });
    }

    onStart(element_id: number) {
        this._service.Start(element_id).then(data => {
            console.log(data);
            this.executionElements = data;
        });
    }

    onAutomatic(element_id: number) {
        this._service.Automatic(element_id).then(data => {
            console.log(data);
            this.executionElements = data;
        });
    }
}