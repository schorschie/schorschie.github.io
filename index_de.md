---
layout: default
title: Lebenslauf
lang: de
ref: index
---

![A portrait of me](/assets/lippe-m.jpg)

&nbsp;

> Hallo, mein Name ist Grzegorz und ich bin ein qualifizierter
> Maschinenbau- und Software-Ingenieur. Ich entwickle und implementiere neue
> Methoden für die Simulation mechanischer und regelungstechnischer Baugruppen.
> Mein Aktuelles Projekt ist die Implementierung von Machine Learning auf
> zeitvarianten Fahrzeugmessreihen.

&nbsp;

## Inhalt

* [Berufstätigkeit](#berufstätigkeit)
* [Programmiererfahrung](#programmiererfahrung)
* [Bildungsweg](#bildungsweg)

&nbsp;

## Berufstätigkeit

*(seit 2020)*
{: .left_time_stamp}

### Systemingenieur

> Systems-Engineering  
> Bosch Automotive Steering GmbH  
> Schwäbisch Gmünd  

Ich bin Data Scientist in Ausbildung und unterstütze das Team bei der
Ausarbeitung der "Operational Design Definition (ODD)" im Rahmen der Requirement
Definition. Zudem verbessere ich die Fähigkeiten in der Softwareentwicklung
durch das bereitstellen eines Continuous Integration Prozesses.

Die wertigsten Beiträge meinerseits sind:

* Entwicklung eines ETL Prozesses für zeitvariante Kundendaten, die aus
  Fahrzeugmessungen im Feld stammen. Diese Daten werden in einer Bosch Datenbank
  gespeichert und erreichen mittlerweile 200+ GB.
* Entwicklung eines Auswerte-Tools mit einer GUI, aber in der Art, dass es gut
  dokumentiert von jedem Bosch Mitarbeiter nach unserer Bosch [Inner
  Source](https://innersourcecommons.org/) Philosophy weiterentwickelt werden
  kann.
* In meinem ersten Data Science Projekt habe ich ein Neuronales Netz entwickelt,
  dass zeitvariante Daten clustert.

*(2017 -- 2020)*
{: .left_time_stamp}

### Entwicklungsingenieur

> Corporate Research  
> Robert Bosch GmbH  
> Renningen  

In einem auf drei Jahre befristetem Vorausentwicklungsprojekt wurden wirksame
Methoden/Prozesse für die simulationsbasierte Freigabe und statistische
Modellvalidierdung formuliert und implementiert.

* Während des Projekts koordinierte ich den Entwicklungsfortschritt mit dem
  Forschungsmanagement des Unternehmens und berichtete alle zwei Monate
  direkt an das Top-Management.
* Ich erwarb umfassende Kenntnisse in agile Methoden sowie eine
  Scrum-Master Schulung und war als Scrum-Master-Proxy tätig.
* Aufbau einer Toolbox für ein Simulations- und Modellqualitäts-Framework, das
  derzeit im Inner Source Hub von Bosch eingesetzt wird.

*(2012 -- 2017)*
{: .left_time_stamp}

### Berechnungsingenieur

> Computer Aided Engineering  
> Bosch Automotive Steering  
> Schwäbisch Gmünd  
> (damals: ZF Lenksysteme GmbH)  

* Auslegung und Lebensdauerberechnung von Verzahnungen, Zahnstangen und
  Kugelgewindetrieben.
* Ein zweiter Schwerpunkt meiner Tätigkeit war die computergestützte
  Modalanalyse an Lenksäulen im NVH Team des CAE-Centers.
* Im ersten Quartal 2015 habe ich eine Task Force geleitet, die Lösungen für NVH
  Probleme bei der Industrialisierung eines Produktes aufgezeigt hat.

*(2010 -- 2012)*
{: .left_time_stamp}

### Projektingenieur

> MesH Engineering Team  
> Dienstleister für die Daimler AG  
> Stuttgart  

* Bei Daimler berechnete ich als Dienstleister Triebstrangschwingungen mit
  SimulationX und Simpack.
* Für das Rennteam der Uni-Stuttgart habe ich Fahrdynamik-Berechnungen für die
  Formula-Student mit Simpack durchgeführt.
* Automatisierte Auswertung von CAN-traces aus Messfahrten und Kompilierung
  aller Analysen in ein LaTeX Dokument.

&nbsp;

## Programmiererfahrung[⇧](#)

*(since 2019)*
{: .left_time_stamp}

### Python und Jupyter

Verwendung von Python, Jupyter und Pandas im Rahmen eines Datenaustauschprojekts mit einem OEM:

* Ich entwickelte den ETL Prozess für Kundendaten von OEM-Fahrzeugen zur
  Bosch-Datenbank.
* Die Daten wurden nach häufigen domänenspezifischen Vorfällen durchsucht, um
  Systemanforderungen und Simulationsmodelle zu verbessern.
* Ich habe ein Machine Learning Algorithmus (Autoencoder) verwendet umd die
  zeitvarianten Daten zu clustern.

*(2018 -- 2019)*
{: .left_time_stamp}

### Python und Pandas

Entwicklung eines Simulationsqualitäts-Framework in Python und Jupyter auf Basis
der Arbeit von Oberkampf & Roy innerhalb eines Vorausentwicklungsprojekts:

* Verwendet Pandas, Matplotlib und Scikit-learn zur Visualisierung statistischer
  Validierungsdaten.
* Einsatz von Bitbucket und Jenkins für Code-Peer-Reviews und automatisierte
  Build-/Testprozesse.
* Akquise neuer Ressourcen über den Bosch Inner Source Hub.

*(2015)*
{: .left_time_stamp}

### NX NASTRAN

Ich habe einen FEM-Checker mit MATLAB für Qualitätstests von NVH-Modellen
entwickelt:

* Das Skript hat die NASTRAN-Quelle des Modells analysiert und die gemeinsamen
  Volumenelemente und Anschlüsse abgeleitet.
* Es Erstellte eine Stückliste mit Bildern der Teile und listete Dichte, Masse
  und Steifigkeit auf, was zur Erstellung einer Visualisierung der Teile und der
  Anschlüsse (Federn, steife Kupplungen) führte.

*(2009)*
{: .left_time_stamp}

### VBA

Während einer Werkstudententätigkeit bei Tata Technologies habe ich einen
Tiefensuchalgorithmus in Visual Basic in CATIA implementiert. Der Algorithmus:

* untersuchte die Struktur eines Kabelbaums mithilfe einer (selbst erstellten)
  Tiefensuche.
* Nach dem Auslesen der Struktur wurde automatisch eine technische Zeichnung mit
  allen Anschlüssen und Kabellängen erstellt.

*(2007)*
{: .left_time_stamp}

### ANSYS

Während meiner Studienarbeit programmierte ich eine kombinierte Elektrodynamik
und Strukturmechanik-Simulation innerhalb eines FE-Modells in
ANSYS in der eigenen APDL Skript-Sprache:

* Zunächst berechnet die Simulation die elektromagnetischen Kräfte auf einen
  Injektor durch das FE-Netz.
* Mithilfe der berechneten Kräfte wurde analytisch die neue Position des
  Injektors bestimmt, das Modell neu vernetzt und die Berechnung wiederholt.

&nbsp;

## Bildungsweg[⇧](#)

*(2022 -- 2023)*
{: .left_time_stamp}

### Bosch Senior Data Scientist

Der Bosch-interne 1,5-jährige Kurs vermittelte mir ein tiefes Expertenwissen zu
Data-Science-Themen, mit einem großen Fokus auf praktisches Wissen und
Projektarbeiten in meiner Abteilung, begleitet von Bosch BCAI-Mentoren.

Der Kurs ist in zwei Teile gegliedert: Junior Expert und Senior Expert. Beide
Teile bestehen jeweils aus "Vor-Ort" Vorlesungen (online seit Corona) und einer
Projektphase. Die in der Junior-Phase der behandelten Themen sind:

* Grundlagen der Statistik
* Statistisches Lernen und Gaußsche Prozesse
* Klassisches maschinelles Lernen
* Deep Learning
* Advanced Deep Learning
* Zeitreihenanalyse

Und in der Senior-Phase:

* ML-Bereitstellung
* Eingebettete KI
* Validierung und Verifizierung / Erklärbare KI
* Dateneffizienz
* Option 1: Spezialisierung auf Sequenzmodelle
* Option 2: Spezialisierung auf Computer Vision
* Foundation-Modelle
* Reinforcement Learning (optional)

*(2021)*
{: .left_time_stamp}

### Machine Learning Engineer Nano-Degree

> Erfahren Sie fortgeschrittene Techniken und Algorithmen für maschinelles
> Lernen und wie Sie Ihre Modelle in einer Produktionsumgebung verpacken und
> bereitstellen. Sammeln Sie praktische Erfahrungen mit Amazon SageMaker, um
> geschulte Modelle in einer Webanwendung bereitzustellen und die Leistung Ihrer
> Modelle zu bewerten. Testen Sie A / B-Modelle und lernen Sie, wie Sie die
> Modelle aktualisieren, wenn Sie mehr Daten erfassen. Dies ist eine wichtige
> Fähigkeit in der Industrie.
> [[Udacity](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t),
> maschinell übersetzt mit [google](https://translate.google.com)]

In einem Projekt bei Bosch/AS kam es zu einem Bezug zum maschinellen Lernen und
ich konnte die Gelegenheit nutzen um mich in diesem Feld zu bilden. Daher habe
ich zu Beginn des Jahres diese Online Schulung
[absolviert](https://confirm.udacity.com/CGALRCZP).

Mein Abschlussprojekt für den Nanodegree, ein
[CNN](https://de.wikipedia.org/wiki/Convolutional_Neural_Network) das
Hunderassen mit >80% genauigkeit erkennt ist auf
[github](https://github.com/schorschie/udacity_dog_breed) veröffentlicht.

*(Frühjahr 2020)*
{: .left_time_stamp}

### Data Analyst Nano-Degree

Während der COVID-19 Pandemie war ich in Kurzarbeit. In meiner neu gewonnenen
Freizeit habe ich diese Webseite geschrieben und investierte einen weiteren Teil
in das Udacity Data Analyst Nano-Degree Programm.

> Diese Schulung bereitet auf eine Karriere als Datenanalyst vor, indem es
> hilft, Daten zu organisieren, Muster und Erkenntnisse aufzudecken,
> aussagekräftige Schlussfolgerungen zu ziehen und kritische Ergebnisse klar zu
> kommunizieren. Es werden Kenntnisse in Python und seinen
> Datenanalysebibliotheken (Numpy, Pandas, Matplotlib) und SQL entwickelt,
> und ein Portfolio von Projekten erstellt.
> [[Udacity](https://www.udacity.com/course/data-analyst-nanodegree--nd002)]

Ich habe den Kurs im Juni 2020
[abgeschlossen](https://graduation.udacity.com/confirm/GMHQJMC3).
Meine bereits vorhandenen Kenntnisse in Jupyter, matplotlib und der
statmodels toolbox konnte ich ausbauen und auf die gelernten
Hypothesen-Testmethoden anwenden. Die Udacity-Projekte kann man auf meinem
[Github repository](https://github.com/schorschie/udacity) einsehen.

*(2003 -- 2009)*
{: .left_time_stamp}

### Studium der Fahrzeug- und Motorentechnik

> Dipl.-Ing. Fahrzeug- und Motorentechnik  
> Universität Stuttgart  
> Stuttgart  

**Hauptfächer:**  Fahrzeugtechnik und Kfz-Mechatronik mit Fokus auf Fahrdynamik
/ Simulation.

**Diplomarbeit:** Modellbildung und Simulation eines automatisierten
Nutzfahrzeuggetriebes

In meiner Diplomarbeit bei der Daimler AG simulierte ich ein nicht synchronisiertes
16-stufiges Nutzfahrzeuggetriebe mit Vorgelegewellenbremse in SimulationX und
Matlab, mit dem Ziel, die Anzahl der Schaltabbrüche zu minimieren.

*(2002 -- 2003)*
{: .left_time_stamp}

### Zivildienst

> Verein zur Förderung spastisch gelähmter  
> Kinder und anderer Körperbehinderter e.V.  
> Nürnberg  
> (heute: Verein für Menschen mit Körperbehinderung Nürnberg e.V.)  

Während dem Zivildienst habe ich gelernt Verantwortung für meine Gemeinschaft,
andere Menschen und mich selbst zu übernehmen. Ich half behinderten Kindern oder
gebrechlichen Älteren in ihrem Alltag, auf ihrem Schulweg, beim Arztbesuch oder beim
Einkauf. Immer zuverlässig und pünktlich.

*(bis 2002)*
{: .left_time_stamp}

### Schulabschluss mit der Allgemeinen Hochschulreife

> Wilhelm Löhe Schule  
> Nürnberg  

**Schriftliche Prüfung:** Mathematik und Erdkunde (LK), sowie Chemie (GK).

**Mündlich:** Deutsch (GK).

Während der Schulzeit engagierte ich mich als Fotograph für die Schülerzeitung
sowie im Schulchor.
