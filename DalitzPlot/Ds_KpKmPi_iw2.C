void Ds_KpKmPi_iw2() {

   // Проверяем подключена ли библиотека генератора распадов, если нет, то подключаем
   //if (!gROOT->GetClass("TGenPhaseSpace")) gSystem->Load("libPhysics");

   // Создаем начальную частицу используя данные PDG
   // Начальной частице соответствует 4х-вектор с нулевыми компонентами импульса Ds мезона
   // http://pdg8.lbl.gov/rpp2013v2/pdgLive/Particle.action?node=S034
   TLorentzVector Ds(0.0, 0.0, 0.0, 1.96850);



   // Создаем объект двухмерная гистограмма (класс TH2F)
   // 1000 бинов по  осям X и Y от  0 до 2 GeV/c^{2}
   TH2F *histogram = new TH2F("histogram","Dalitz plot; M_{inv}(K^{+}K^{-}) GeV; M_{inv}(K^{-}pi^{+}) GeV", 1000, 0., 2., 1000, 0., 2.);


//-------------------------------------------------------------------------------------
//   Ds+ -> pi+ K+ K-
//-------------------------------------------------------------------------------------

   // Подготавливаем генератор нерезонансного распада
   // создаем массив куда записываем соответствующие массы
   Double_t masses_non_res[3] = { 0.493, 0.493, 0.139} ;

   // Объявляем 4х-вектора конечных частиц
   // чтобы пользоваться ими потом
   TLorentzVector vKp;
   TLorentzVector vKm;
   TLorentzVector vPi;

   // Создаем объект генератор
   TGenPhaseSpace event;

   // Устанавливаем распад
   event.SetDecay(Ds, 3, masses_non_res);

   // Генерируем события НЕРЕЗОНАНСНОГО  распада
   Int_t gen_events=0;
   while (gen_events<100000) {

      // При генерации каждому событию приписывается вес от 0 до 1
      // этот вес пропорционален вероятности появления данного события
      Double_t weight = event.Generate();


      // Забираем указатели на 4х-вектора
      TLorentzVector *p1 = event.GetDecay(0);
      TLorentzVector *p2 = event.GetDecay(1);
      TLorentzVector *p3 = event.GetDecay(2);

      vKp = *p1;
      vKm = *p2;
      vPi = *p3;

      // Для каждого десятитысячного события выводим на экран его вес
      if(  !(gen_events%10000) ) 
      {
        cout << weight << endl;
      }
      // заполняем гистограмму
      // Можем заполнять с весами, но лучше сделать пособытийно
      if(gRandom->Rndm() < weight){
         histogram->Fill( (vKp+vKm).M() , (vKm+vPi).M());
         gen_events++;
        }
   }


//-------------------------------------------------------------------------------------
//   Ds -> pi phi(->KK)
//-------------------------------------------------------------------------------------

   // Объявляем 4х-вектор промежуточного резонанса
   // чтобы пользоваться ими потом
   TLorentzVector vPhi;


   // Подготавливаем генератор распада Ds+ -> phi pi+
   Double_t masses_phi[2] = { 1.020, 0.139} ;
   TGenPhaseSpace event_phi_pi;
   event_phi_pi.SetDecay(Ds, 2, masses_phi);

   // Подготавливаем генератор распада phi -> K+ K-
   Double_t masses_KK[2] = { 0.493, 0.493} ;
   TGenPhaseSpace event_KK;

   // Генерируем события РЕЗОНАНСНОГО распада
   gen_events=0;
   while (gen_events<100000) {

      // Генерируем распад Ds --> pi phi
      Double_t weight_phi = event_phi_pi.Generate();
      TLorentzVector *p1 = event_phi_pi.GetDecay(0);
      TLorentzVector *p2 = event_phi_pi.GetDecay(1);
      vPhi = *p1;
      vPi = *p2;


      // Генерируем распад phi --> K+ K-
      event_KK.SetDecay(vPhi, 2, masses_KK);
      Double_t weight_KK = event_KK.Generate();
      TLorentzVector *pp1 = event_KK.GetDecay(0);
      TLorentzVector *pp2 = event_KK.GetDecay(1);
      vKp = *pp1;
      vKm = *pp2;

      // Для каждого десятитысячного события выводим на экран его вес
      if(  !(gen_events%10000) ) cout << weight_phi << endl;

      // Заполняем гистограмму
      // Можем заполнять с весами, но лучше сделать пособытийно
      if(gRandom->Rndm()<weight_KK*weight_phi){
         histogram->Fill( (vKp+vKm).M() , (vKm+vPi).M());
         gen_events++;
        }
   }


//-------------------------------------------------------------------------------------
// Добавтье сюда код для генерации еще одного резонанса по примеру Ds-> pi phi
//-------------------------------------------------------------------------------------


//=====================================================================================

   // Выводим гистограмму на экран
   histogram->Draw("colz");
   // Изучите опции вывода!


}
