import { makeAutoObservable } from "mobx";

export default class DeviceStore {
  private _types: any[] = [];
  private _authors: any[] = [];
  private _devices: any[] = [];
  private _selectedType: any = {};
  private _selectedBrand: any = {};
  private _page: number = 1;
  private _totalCount: number = 0;
  private _limit: number = 3;

  constructor() {
    makeAutoObservable(this);
  }

  setTypes(types: any[]) {
    this._types = types;
  }
  setAuthors(authors: any[]) {
    this._authors = authors;
  }
  setDevices(devices: any[]) {
    this._devices = devices;
  }

  setSelectedType(type: any) {
    this.setPage(1);
    this._selectedType = type;
  }
  setSelectedBrand(brand: any) {
    this.setPage(1);
    this._selectedBrand = brand;
  }
  setPage(page: number) {
    this._page = page;
  }
  setTotalCount(count: number) {
    this._totalCount = count;
  }

  get types() {
    return this._types;
  }
  get authors() {
    return this._authors;
  }
  get devices() {
    return this._devices;
  }
  get selectedType() {
    return this._selectedType;
  }
  get selectedBrand() {
    return this._selectedBrand;
  }
  get totalCount() {
    return this._totalCount;
  }
  get page() {
    return this._page;
  }
  get limit() {
    return this._limit;
  }
}
