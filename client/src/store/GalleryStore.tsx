import { makeAutoObservable } from "mobx"

type Gallery = {
    // define the user type here
}

export default class GalleryStore {
    setSelectedType(type: any): void {
        throw new Error('Method not implemented.')
    }
    _types: Gallery[] = [
        { id: 1, name: 'Refrigerator' },
        { id: 2, name: 'Planet' }
    ]
    _authors: Gallery[] = [
        { id: 1, name: 'x1' },
        { id: 2, name: 'x2' }
    ]
    _photos: Gallery[] = [
        { id: 1, name: 'Outer Planet', price: 1000, rating: 5, img: '' },
        { id: 2, name: 'Planet', price: 123, rating: 5, img: '' },
        { id: 3, name: 'Outer', price: 4, rating: 5, img: '' },
        { id: 4, name: 'Space', price: 23, rating: 5, img: '' }
    ]
    constructor() {
        makeAutoObservable(this)
    }

    setTypes(value: Gallery[]) {
        this._types = value
    }

    setAuthors(value: Gallery[]) {
        this._authors = value
    }
    setPhotos(value: Gallery[]) {
        this._photos = value
    }
}
