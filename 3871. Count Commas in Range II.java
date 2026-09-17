You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
  class Solution {
    public long countCommas(long n) {
        if (n <= 999) return 0;

        long totalCommas = 0;
        long rangeStart = 1000;
        long rangeEnd = rangeStart * 1000 - 1;
        int commas = 1;

        while (rangeStart <= n) {
            long numbers = Math.min(n, rangeEnd) - rangeStart + 1;
            totalCommas += (long) commas * numbers;

            if (rangeEnd > n) break;

            rangeStart = rangeStart * 1000;
            rangeEnd = rangeStart * 1000 - 1;
            commas++;
        }
        return totalCommas;
    }
}
