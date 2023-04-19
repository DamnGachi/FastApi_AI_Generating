import { $authHost, $host } from "./index";
import jwt_decode from "jwt-decode";

export const createType = async (type: any) => {
    const { data } = await $authHost.post('api/type', type)
    return data
}

export const fetchTypes = async () => {
    const { data } = await $host.get('api/type')
    return data
}

export const createBrand = async (brand: any) => {
    const { data } = await $authHost.post('api/brand', brand)
    return data
}

export const fetchAuthors = async () => {
    const { data } = await $host.get('api/brand',)
    return data
}

export const createPhotoCard = async (photocard: any) => {
    const { data } = await $authHost.post('api/photocard', photocard)
    return data
}

export const fetchPhotoCards = async (typeId: any, brandId: any, page: any, limit = 5) => {
    const { data } = await $host.get('api/photocard', {
        params: {
            typeId, brandId, page, limit
        }
    })
    return data
}

export const fetchOnePhotoCard = async (id: any) => {
    const { data } = await $host.get('api/photocard/' + id)
    return data
}
