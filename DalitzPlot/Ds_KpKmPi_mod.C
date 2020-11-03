void Ds_KpKmPi_mod() {

   // Проверяем подключена ли библиотека генератора распадов, если нет, то подключаем
   //if (!gROOT->GetClass("TGenPhaseSpace")) gSystem->Load("libPhysics");

   // Создаем начальную частицу используя данные PDG
   // Начальной частице соответствует 4х-вектор с нулевыми компонентами импульса Ds мезона
   // http://pdg8.lbl.gov/rpp2013v2/pdgLive/Particle.action?node=S034
   TLorentzVector Ds(0.0, 0.0, 0.0, 2.81673);
   //TLorentzVector Ds(0.0, 0.0, 0.0, 2.81673);


   // Создаем объект двухмерная гистограмма (класс TH2F)
   // 1000 бинов по  осям X и Y от  0 до 2 GeV/c^{2}
   TH2F *histogram = new TH2F("histogram","Dalitz plot; M_{inv}(Ksi(2470)+Pi]) GeV; M_{inv}(Pi + Pi) GeV", 1000, 2.64, 2.65, 1000, 0.27, 0.35);


//-------------------------------------------------------------------------------------
//   Ds -> pi phi(->KK)
//-------------------------------------------------------------------------------------

   // Объявляем 4х-вектор промежуточного резонанса
   // чтобы пользоваться ими потом
   TLorentzVector vKsi2470;
   TLorentzVector vPi;
   TLorentzVector vPi2;
   TLorentzVector vKsi2645;


   // Подготавливаем генератор распада Ksi2815 -> Ksi2645 pi+
   Double_t masses_phi[2] = { 2.64557, 0.13957} ;
   TGenPhaseSpace event_phi_pi;
   event_phi_pi.SetDecay(Ds, 2, masses_phi);

   // Подготавливаем генератор распада Ksi2645 -> KsiGS+ Pi
   Double_t masses_KK[2] = { 2.46793, 0.13957} ;
   TGenPhaseSpace event_KK;

   // Генерируем события РЕЗОНАНСНОГО распада
   Int_t gen_events=0;
   while (gen_events<100000) {

      // Генерируем распад Ds --> p phi
      Double_t weight_phi = event_phi_pi.Generate();
      TLorentzVector *p1 = event_phi_pi.GetDecay(0);
      TLorentzVector *p2 = event_phi_pi.GetDecay(1);
      vKsi2645 = *p1;
      vPi = *p2;


      // Генерируем распад 2645 --> Pi+ KsiGs
      event_KK.SetDecay(vKsi2645, 2, masses_KK);
      Double_t weight_KK = event_KK.Generate();
      TLorentzVector *pp1 = event_KK.GetDecay(0);
      TLorentzVector *pp2 = event_KK.GetDecay(1);

      vKsi2470 = *pp1;
      vPi2 = *pp2;

      // Для каждого десятитысячного события выводим на экран его вес
      if(  !(gen_events%10000) ) cout << weight_phi << endl;
      if(  !(gen_events%10000) ) cout << weight_KK << endl;
      // Заполняем гистограмму
      // Можем заполнять с весами, но лучше сделать пособытийно
      if(gRandom->Rndm()<weight_KK*weight_phi){
         histogram->Fill( (vKsi2470+vPi2).M() , (vPi2+vPi).M());
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
