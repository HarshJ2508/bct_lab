// npm install web3
const Web3 = require('web3').default;

const web3 = new Web3('http://localhost:8545');

const senderAccount = '0x0dc7eB341509ed2825A3AA13Da9DE455602Bc830'; 
const receiverAccount = '0xa03F8d8f08c1a4becc3dCA6B1B04E9d46AcAC04d';

const sendEther = async () => {
  try {
    
    const balanceBefore = await web3.eth.getBalance(senderAccount);
    console.log(`Sender Balance before: ${web3.utils.fromWei(balanceBefore, 'ether')} ETH`);
    const tx = {
      from: senderAccount,
      to: receiverAccount,
      value: web3.utils.toWei('0.1', 'ether'),
      gas: 21000, 
      gasPrice: await web3.eth.getGasPrice(), 
    };
    const receipt = await web3.eth.sendTransaction(tx);
    console.log('Transaction successful:', receipt);
    const balanceAfter = await web3.eth.getBalance(senderAccount);
    console.log(`Sender Balance after: ${web3.utils.fromWei(balanceAfter, 'ether')} ETH`);

    getLatestBlock();
    getSpecificBlock(1);
    getAllBlocks();
  } catch (error) {
    console.error('Error sending transaction:', error);
  }
};
sendEther();

async function getLatestBlock() {
    try {
        const latestBlockNumber = await web3.eth.getBlockNumber();
        const block = await web3.eth.getBlock(latestBlockNumber, true);
        console.log('\nLatest block details:', block);
    } catch (error) {
        console.error('Error fetching latest block:', error);
    }
}


async function getSpecificBlock(blockNumber) {
    try {
        const block = await web3.eth.getBlock(blockNumber, true);
        console.log(`\nBlock ${blockNumber} details:`, block);
    } catch (error) {
        console.error(`Error fetching block ${blockNumber}:`, error);
    }
}

const formatBigInt = (value) => {
    if (typeof value === 'bigint') {
        return value.toString();
    }
    return value;
};

async function getAllBlocks() {
    try {
        // Get the latest block number
        const latestBlockNumber = await web3.eth.getBlockNumber();
        console.log(`Total number of blocks: ${latestBlockNumber + 1}\n`);

        // Fetch all blocks from 0 to latest
        for (let i = 0; i <= latestBlockNumber; i++) {
            const block = await web3.eth.getBlock(i, true);
            
            console.log(`\n====== Block ${i} ======`);
            console.log({
                blockNumber: formatBigInt(block.number),
                blockHash: block.hash,
                timestamp: new Date(Number(block.timestamp) * 1000).toLocaleString(),
                miner: block.miner,
                difficulty: formatBigInt(block.difficulty),
                totalDifficulty: formatBigInt(block.totalDifficulty),
                gasUsed: formatBigInt(block.gasUsed),
                gasLimit: formatBigInt(block.gasLimit),
                nonce: formatBigInt(block.nonce),
                transactions: block.transactions.map(tx => ({
                    hash: tx.hash,
                    from: tx.from,
                    to: tx.to,
                    value: web3.utils.fromWei(formatBigInt(tx.value), 'ether') + ' ETH',
                    gas: formatBigInt(tx.gas),
                    gasPrice: web3.utils.fromWei(formatBigInt(tx.gasPrice), 'gwei') + ' Gwei'
                })),
                transactionCount: block.transactions.length,
                size: formatBigInt(block.size),
                parentHash: block.parentHash
            });

            // If block has transactions, show detailed transaction info
            if (block.transactions.length > 0) {
                console.log('\nTransactions in this block:');
                block.transactions.forEach((tx, index) => {
                    console.log(`\nTransaction ${index + 1}:`);
                    console.log(`Hash: ${tx.hash}`);
                    console.log(`From: ${tx.from}`);
                    console.log(`To: ${tx.to}`);
                    console.log(`Value: ${web3.utils.fromWei(formatBigInt(tx.value), 'ether')} ETH`);
                    console.log(`Gas Price: ${web3.utils.fromWei(formatBigInt(tx.gasPrice), 'gwei')} Gwei`);
                    console.log(`Gas Used: ${formatBigInt(tx.gas)}`);
                });
            }
        }

    } catch (error) {
        console.error('Error fetching blocks:', error);
    }
}