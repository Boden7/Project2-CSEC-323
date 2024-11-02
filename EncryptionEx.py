def _write_transactions(self):
        # Set the Debug Flag
        DEBUG = False
        # Encryption key (Ensure the key is 16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
        key = b'MySuperSecretKey1222222222222222'
        # Initialization vector (Ensure the IV is 16 bytes)
        iv = b'MySuperSecretIV1'

        if DEBUG:
            print("The length of the key is %d bytes" % len(key))
            print("The length of the Initialization Vector is %d bytes" % len(iv))

        # Open the file to write the data
        with open("savings.txt", "wb") as outfile:
            for transaction in self._accountTransactions:
                # Convert transaction to string, then encrypt
                transaction_str = str(transaction)
                # Encrypt the transaction data
                encrypted_data = encrypt_AES_CBC(transaction_str, key, iv)
                # Write the length of the encrypted data to the file
                outfile.write(str(len(encrypted_data)).encode())
                outfile.write(b"\n")
                # Write the encrypted data to the file
                outfile.write(encrypted_data)
                outfile.write(b"\n")

        if DEBUG:
            print("Transactions written to savings.txt.")

    def _read_transactions(self):
        # Set the Debug Flag
        DEBUG = False
        key = b'MySuperSecretKey1222222222222222'
        iv = b'MySuperSecretIV1'

        # Open the file to read the data
        with open("savings.txt", "rb") as infile:
            length = infile.readline().rstrip().decode()

            while length != "":
                length = int(length)
                if DEBUG:
                    print("Length: ", length)
                data = infile.read(length)
                data = decrypt_AES_CBC(data, key, iv)
                # process the decrypted data: 
                print("Decrypted transaction:", data.decode())
                infile.readline()  # Skip the newline
                length = infile.readline().rstrip().decode()



        
