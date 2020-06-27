import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataBaseInfoComponent } from './data-base-info.component';

describe('DataBaseInfoComponent', () => {
  let component: DataBaseInfoComponent;
  let fixture: ComponentFixture<DataBaseInfoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataBaseInfoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataBaseInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
