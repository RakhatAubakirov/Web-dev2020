import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { Vacancy } from '../interfaces';
import { CompanyService } from "../company.service";

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(
    private companyService:CompanyService,
    private route:ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getListOfVacancies();
  }

  getListOfVacancies() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.companyService.getVacancies(id).subscribe(vacancies => this.vacancies = vacancies);
  }

}