import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser'; // Для обычных приложений в браузере
import { AppComponent } from './app.component';
import { CommonModule } from '@angular/common';
@NgModule({
  declarations: [AppComponent],
  imports: [CommonModule], // Убедитесь, что импортирован BrowserModule
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
