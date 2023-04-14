import { makeAutoObservable } from "mobx"

type User = {
  // define the user type here
}

export default class UserStore {
  _isAuth: boolean = true
  _user: User | null = null

  constructor() {
    makeAutoObservable(this)
  }

  setIsAuth(value: boolean) {
    this._isAuth = value
  }

  setUser(value: User) {
    this._user = value
  }
}
