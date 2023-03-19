import styles from './Home.module.css'
function Home() {
    return (
        <div>
            <h1>Mamy Ebal</h1>
            <div>
                <div className={styles.item}>
                    <h1>car 1</h1>
                    <p>$100000</p>
                    <button>buy</button>
                </div>
            </div>
        </div>
    )
}

export default Home
