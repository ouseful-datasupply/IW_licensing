# Specification of the IW Licensing Search API

The Isle of Wight Council licensing search provides searches over:

- licensing applications
- licenses

We can use the following as part of a validator and/or to provide options in user interface components:

__`searchCriteria.applicationType`__:

- `All`: ``
- `New`: `NEW`
- `Reinstatement`: `REI`
- `Renewal`: `REN`
- `Review`: `REV`
- `Transfer`: `TRN`
- `Variation`: `VAR`

__`searchCriteria.ward`__:

- `All`: ``
- `Arreton And Newchurch`: `01`
- `Bembridge`: `47`
- `Binstead And Fishbourne`: `02`
- `Brading And St Helens`: `48`
- `Brading, St. Helens And Bembridge`: `03`
- `Brighstone Calbourne And Shalfleet`: `57`
- `Carisbrooke And Gunville`: `51`
- `Central Rural`: `43`
- `Central Wight`: `05`
- `Chale Niton And Shorwell`: `42`
- `Chale, Niton And Whitwell`: `06`
- `Cowes Medina`: `07`
- `Cowes North`: `08`
- `Cowes South And Northwood`: `09`
- `Cowes West And Gurnard`: `10`
- `East Cowes`: `11`
- `EXPIRED - Ashey`: `AE`
- `EXPIRED - Bembridge North`: `BEN`
- `EXPIRED - Bembridge South`: `BES`
- `EXPIRED - Binstead`: `BNS`
- `EXPIRED - Brading And St Helens`: `BSTH`
- `EXPIRED - Brighstone And Calbourne`: `BRCA`
- `EXPIRED - Calb Shalfleet And Yarmouth`: `CSY`
- `EXPIRED - Carisbrooke East`: `CAE`
- `EXPIRED - Carisbrooke West`: `CAW`
- `EXPIRED - Central Rural`: `CENR`
- `EXPIRED - Cowes Castle East`: `CCE`
- `EXPIRED - Cowes Castle West`: `CCW`
- `EXPIRED - Cowes Central`: `CC`
- `EXPIRED - East Cowes North`: `ECN`
- `EXPIRED - East Cowes South`: `ECS`
- `EXPIRED - Fairlee`: `FL`
- `EXPIRED - Freshwater Afton`: `FRA`
- `EXPIRED - Freshwater Norton`: `FRN`
- `EXPIRED - Gurnard`: `GN`
- `EXPIRED - Mount Joy`: `MJ`
- `EXPIRED - Newchurch`: `NEWC`
- `EXPIRED - Northwood`: `NW`
- `EXPIRED - Osborne`: `OS`
- `EXPIRED - Pan`: `PAN`
- `EXPIRED - Ryde South East`: `RYSE`
- `EXPIRED - Ryde South West`: `RYSW`
- `EXPIRED - Ryde St Johns East`: `RSJE`
- `EXPIRED - Ryde St Johns West`: `RSJW`
- `EXPIRED - Shalfleet And Yarmouth`: `SHAY`
- `EXPIRED - Shanklin North`: `SHN`
- `Fairlee And Whippingham`: `58`
- `Freshwater North And Yarmouth`: `52`
- `Freshwater South`: `13`
- `Godshill And Wroxall`: `14`
- `Havenstreet, Ashey And Haylands`: `15`
- `Haylands And Swanmore`: `49`
- `Lake North`: `16`
- `Lake South`: `17`
- `Mountjoy And Shide`: `44`
- `Nettlestone And Seaview`: `18`
- `Newchurch Havenstreet And Ashey`: `50`
- `Newport Central`: `19`
- `Newport North`: `21`
- `Newport West`: `23`
- `Osborne`: `59`
- `Pan And Barton`: `46`
- `Parkhurst`: `24`
- `Parkhurst And Hunnyhill`: `54`
- `Ryde Appley And Elmfield`: `56`
- `Ryde Monktonmead`: `55`
- `Ryde North East`: `26`
- `Ryde North West`: `27`
- `Ryde South East`: `53`
- `Ryde West`: `29`
- `Sandown North`: `30`
- `Sandown South`: `31`
- `Shanklin Central`: `32`
- `Shanklin South`: `33`
- `Totland`: `34`
- `Totland And Colwell`: `45`
- `Ventnor And St Lawrence`: `40`
- `Ventnor East`: `35`
- `Ventnor West`: `36`
- `West Wight`: `37`
- `Wootton`: `39`
- `Wroxall Lowtherville And Bonchurch`: `41`</select>

__`searchCriteria.categoryType`__:

- `All`: ``
- `Animal Welfare`: `Animal`
- `Caravans`: `Caravans`
- `Charitable Collections`: `Charitable`
- `Driver`: `Driver`
- `Gaming Permits`: `Gaming`
- `Houses in Multiple Occupation`: `HMO`
- `Operator`: `Operator`
- `Other`: `LicensingOther`
- `Personal`: `Personal`
- `Premises`: `Premises`
- `Sex Establishments`: `Sex`
- `Street Trading`: `Street`
- `Temporary Event Notices`: `TEN`
- `Vehicle (Hackney Carriage)`: `Hackney`
- `Vehicle (Private Hire)`: `PrivateHire`</select>



__`searchCriteria.activityFormField`__:

- `All`: ``
- `Band A - 0 to £4300`: `LIPERMIT.BANDA`
- `Band B - £4301 to £33000`: `LIPERMIT.BANDB`
- `Band C - £33001 to £87000`: `LIPERMIT.BANDC`
- `Boxing or Wrestling Entertainment`: `LIPERMIT.BOXING`
- `Entertainment of a Similar Description`: `LIPERMIT.SIMILA`
- `Excluded from EMRO`: `LIPERMIT.EMROEX`
- `Exempt from Banding`: `LIPERMIT.BANDEX`
- `Films`: `LIPERMIT.FILMS`
- `House to House`: `LIPERMIT.H2HOUS`
- `Included in EMRO`: `LIPERMIT.EMRO`
- `Indoor Sporting Event`: `LIPERMIT.INDSPO`
- `Late Night Refreshment`: `LIPERMIT.LATEN`
- `Live Music`: `LIPERMIT.LIVEM`
- `Market Organiser`: `LIPERMIT.MRKOR`
- `Market Trader 1`: `LIPERMIT.MRK1`
- `Market Trader 10`: `LIPERMIT.MRK10`
- `Market Trader 11`: `LIPERMIT.MRK11`
- `Market Trader 12`: `LIPERMIT.MRK12`
- `Market Trader 13`: `LIPERMIT.MRK13`
- `Market Trader 14`: `LIPERMIT.MRK14`
- `Market Trader 15`: `LIPERMIT.MRK15`
- `Market Trader 16`: `LIPERMIT.MRK16`
- `Market Trader 17`: `LIPERMIT.MRK17`
- `Market Trader 18`: `LIPERMIT.MRK18`
- `Market Trader 19`: `LIPERMIT.MRK19`
- `Market Trader 2`: `LIPERMIT.MRK2`
- `Market Trader 20`: `LIPERMIT.MRK20`
- `Market Trader 21`: `LIPERMIT.MRK21`
- `Market Trader 22`: `LIPERMIT.MRK22`
- `Market Trader 23`: `LIPERMIT.MRK23`
- `Market Trader 24`: `LIPERMIT.MRK24`
- `Market Trader 25`: `LIPERMIT.MRK25`
- `Market Trader 26`: `LIPERMIT.MRK26`
- `Market Trader 27`: `LIPERMIT.MRK27`
- `Market Trader 28`: `LIPERMIT.MRK28`
- `Market Trader 29`: `LIPERMIT.MRK29`
- `Market Trader 3`: `LIPERMIT.MRK3`
- `Market Trader 4`: `LIPERMIT.MRK4`
- `Market Trader 5`: `LIPERMIT.MRK5`
- `Market Trader 6`: `LIPERMIT.MRK6`
- `Market Trader 7`: `LIPERMIT.MRK7`
- `Market Trader 8`: `LIPERMIT.MRK8`
- `Market Trader 9`: `LIPERMIT.MRK9`
- `Mobile Street Trader`: `LIPERMIT.MOBSTR`
- `Performance of Dance`: `LIPERMIT.DANCEP`
- `Play`: `LIPERMIT.PLAY`
- `Recorded Music`: `LIPERMIT.RECOM`
- `Sale of Alcohol by Retail`: `LIPERMIT.RETALC`
- `Static Street Trader`: `LIPERMIT.STASTR`
- `Street Collection`: `LIPERMIT.STREET`
- `Street Furniture`: `LIPERMIT.STFURN`
- `Supply of Alcohol`: `LIPERMIT.SUPALC`
- `£125001 +`: `LIPERMIT.BANDE`
- `£87001 to £125000`: `LIPERMIT.BANDD`</select>

__`searchCriteria.timePeriod`__:

- `All`: ``
- `5th November`: `5NOV`
- `Bank Holiday Sundays`: `BHSUN`
- `Christmas Eve`: `CHREVE`
- `Friday`: `05_FRI`
- `Friday and Saturday`: `FRISAT`
- `Friday or Saturday`: `FROSAT`
- `Friday to Sunday`: `FRISUN`
- `Mon Wed Thurs Fri Saturday`: `MWTFSA`
- `Monday`: `01_MON`
- `Monday and Saturday`: `MOSAT`
- `Monday and Tuesday`: `MONTUE`
- `Monday to Friday`: `MONFRI`
- `Monday to Saturday`: `MONSAT`
- `Monday to Sunday`: `10_M2S`
- `Monday to Thursday`: `MONTHU`
- `Monday to Wednesday`: `MONWED`
- `Monday Tuesday Thursday Sunday`: `MTTHSU`
- `Monday Wednesday Thursday Friday Sunday`: `MWTFS`
- `New Year's Eve`: `NYE`
- `Saturday`: `06_SAT`
- `Saturday and Sunday`: `SATSUN`
- `Sunday`: `07_SUN`
- `Sunday Monday and Wednesday`: `SUMOWE`
- `Sunday to Friday`: `SUNFRI`
- `Sunday to Thursday`: `09_S2T`
- `Sunday to Tuesday`: `SUNTUE`
- `Sunday to Wednesday`: `SUNWED`
- `Thursday`: `04_THU`
- `Thursday and Friday`: `THUFRI`
- `Thursday to Saturday`: `08_T2S`
- `Thursday to Saturday`: `THUSAT`
- `Thursday to Sunday`: `THUSUN`
- `Thursday to Tuesday`: `THUTUE`
- `Tuesday`: `02_TUE`
- `Tuesday and Wednesday`: `TUEWED`
- `Tuesday Saturday`: `TUESA`
- `Tuesday to Saturday`: `TUESAT`
- `Tuesday to Sunday`: `TUESUN`
- `Wednesday`: `03_WED`
- `Wednesday and Thursday`: `WEDTHU`
- `Wednesday Friday and Saturday`: `WEFRSA`
- `Wednesday to Friday`: `WEDFRI`
- `Wednesday to Monday`: `WEDMON`
- `Wednesday to Saturday`: `WEDSAT`</select>

__`searchCriteria.caseDecision`__:

- `All`: ``
- `Grant Licence`: `GRANT`
- `Grant with Conditions`: `CON`
- `Refuse and Refer LA Decision to DBS`: `DBSREF`
- `Refuse Licence`: `REFUSE`
- `Withdrawn`: `WITH`


## Licensing application

https://publicaccess.iow.gov.uk/online-applications/search.do?action=advanced&searchType=LicencingApplication


__`searchCriteria.caseStatus`__:

- `All`: ``
- `New`: `New`
- `Open for Consultation`: `Open for Consultation`
- `Pending Decision`: `Pending Decision`</select>

searchCriteria.reference: 
searchCriteria.alternativeReference: 
searchCriteria.applicantName: 
searchCriteria.applicationType: 
searchCriteria.categoryType: 
searchCriteria.ward: 
searchCriteria.agent: 
searchCriteria.caseStatus: 
searchCriteria.tradingName: 
searchCriteria.caseDecision: 
caseAddressType: Application
searchCriteria.address: 
searchCriteria.plateNumber: 
searchCriteria.registrationNumber: 
searchCriteria.vehicleMake: 
searchCriteria.vehicleModel: 
searchCriteria.activityFormField: 
searchCriteria.timePeriod: 
searchCriteria.openTime: 
searchCriteria.closeTime: 
date(receivedStart): 13/02/2025
date(receivedEnd): 
searchType: LicencingApplication

Searchtype: `LicencingApplication`

## Licenses


https://publicaccess.iow.gov.uk/online-applications/search.do?action=advanced&searchType=Licencing


__`searchCriteria.caseStatus`__:

- `All`: ``
- `Current Licence`: `Current Licence`
- `Licence Under Review`: `Licence Under Review`</select>



searchCriteria.reference: 
searchCriteria.alternativeReference: 
searchCriteria.applicantName: 
searchCriteria.applicationType: 
searchCriteria.categoryType: 
searchCriteria.ward: 
searchCriteria.agent: 
searchCriteria.caseStatus: 
searchCriteria.tradingName: 
searchCriteria.caseDecision: 
searchCriteria.address: 
searchCriteria.plateNumber: 
searchCriteria.registrationNumber: 
searchCriteria.vehicleMake: 
searchCriteria.vehicleModel: 
searchCriteria.activityFormField: 
searchCriteria.timePeriod: 
searchCriteria.openTime: 
searchCriteria.closeTime: 
date(issuedStart): 12/02/2025
date(issuedEnd): 
date(durationStart): 
date(durationEnd): 
date(hearingStart): 
date(hearingEnd): 
searchType: Licencing

Searchtype: `Licencing`


## Results

Summary

- Reference
- Type
- Category
- Status
- Applicant
- Trading Name
- Address
- Issue Date
- Expiry Date
- Case Officer
