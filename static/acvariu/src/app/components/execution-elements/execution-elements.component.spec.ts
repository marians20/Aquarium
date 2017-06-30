import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExecutionElementsComponent } from './execution-elements.component';

describe('ExecutionElementsComponent', () => {
  let component: ExecutionElementsComponent;
  let fixture: ComponentFixture<ExecutionElementsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExecutionElementsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExecutionElementsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
