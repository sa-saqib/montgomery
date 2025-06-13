
# Bezout's identity : a and b be two non-zero integers with z being their g.c.d, then there exists integers x and y such that  a (x) + b (y) = z.
# These x & y are known as bezout's coefficients. we can get these coefficients by extended ecludian algorithm, Blankinship algorithm, etc
# below is the link provided to have a look at Blankinship's algorithm
# https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Clark)/01%3A_Chapters/1.09%3A_Blankinship's_Method

def get_coefficients(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    
    while b != 0:  
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0

"""getting coefficients for p-256"""

# from the reference of https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-186.pdf
# under section 3.2.1.3. P-256 our prime number N is 2^256 − 2^224 + 2^192 + 2^96 − 1
# which is same as 115792089210356248762697446949407573530086143415290314195533631308867097853951
N =  115792089210356248762697446949407573530086143415290314195533631308867097853951 
# R is 2^256 because it is the nearest power of 2 greater than N. Re writing our prime number as [(2^256 -1)+(-2^224 +2^192 +2^96)]
# As (-2^224 +2^192 +2^96) is negative and also 2^256-1 is less than 2^256. we can take R as 2^256.
R = pow(2,256)

gcd, n_inv, r_inv = get_coefficients(N, R) 
print(f"GCD: {gcd}, \n Bézout's coefficients: n_inv = {n_inv}, \n r_inv = {r_inv}\n")
# n_inv = 26959946654596436323893653559348051827142583427821597254581997273087 ,        r_inv = -26959946648319334592891477706824406424704094582978235142356758167551
#       = 0xfffffffdfffffffffffffffffffffffeffffffffffffffffffffffff                    r_inv = -0xfffffffd00000002fffffffdffffffff00000001fffffffcffffffff


"""getting coefficients for p-384"""

# from the reference of https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-186.pdf
# under section 3.2.1.4. P-384. our prime number N1 is 2^384 − 2^128 − 2^96 + 2^32 − 1
# which is same as 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
N1 = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
R1 = pow(2,384)

gcd, n1_inv, r1_inv = get_coefficients(N1, R1) 
print(f"GCD: {gcd}, Bézout's coefficients: n1_inv = {n1_inv}, \nr1_inv = {r1_inv}\n")
# n1_inv = -183479889321925461653251752109332205360611897149516305954304919627392402791262062194444675036228396293029889
# n1_inv = -0x14000000140000000c00000002fffffffcfffffffafffffffbfffffffe00000000000000010000000100000001

# r1_inv = 183479889321925461653251752109332205360611897149516305954304919627392402791260477631193651879713439593005062
# r1_inv = x14000000140000000c00000002fffffffcfffffffafffffffbfffffffdffffffebffffffd8ffffffe100000006



"""getting coefficients for p-521"""

# from the reference of https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-186.pdf
# under section 3.2.1.5. P-521. our prime number N is 2^521 − 1.
# N2 is 2^521 - 1; our R2 will be 2^521 which is a power of 2 and gretaer than N2 .
N2 = pow(2,521) - 1
R2 = pow(2,521)

gcd, n2_inv, r2_inv = get_coefficients(N2, R2) 
print(f"GCD: {gcd}, Bézout's coefficients: n2_inv = {n2_inv}, \n r2_inv = {r2_inv}")
# n2_inv = -1         # r2_inv = 1



