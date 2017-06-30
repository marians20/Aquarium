import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './components/app.component';
import { NavmenuComponent } from './components/navmenu/navmenu.component';
import { FooterComponent } from './components/footer/footer.component';
import { MainComponent } from './components/main/main.component';

import { ExecutionElementsService } from './services/execution-elements.service';
import { ExecutionElementsComponent } from './components/execution-elements/execution-elements.component';

@NgModule({
  declarations: [
    AppComponent,
    NavmenuComponent,
    FooterComponent,
    MainComponent,
    ExecutionElementsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
            { path: '', redirectTo: 'home', pathMatch: 'full' },
            { path: 'main', component: MainComponent },
            { path: 'execution-elements', component: ExecutionElementsComponent },
            { path: '**', redirectTo: 'home' }
        ])
  ],
  providers: [
        { provide: 'ORIGIN_URL', useValue: location.origin },
        ExecutionElementsService
        ],
  bootstrap: [AppComponent]
})
export class AppModule { }
