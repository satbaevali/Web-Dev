import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [CommonModule]  
})
export class AppComponent {
  companies = [{title: 'Google'}, {title: 'Amazon'}]; 
}
