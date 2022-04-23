public class Codec {

  private HashMap<String, String> map = new HashMap<>();
  private final static String base = "http://tiniurl.com/";

  // Encodes a URL to a shortened URL.
  public String encode(String longUrl) {
    String hash = String.valueOf(longUrl.hashCode());
    map.put(hash, longUrl);
    return base + hash;
  }

  // Decodes a shortened URL to its original URL.
  public String decode(String shortUrl) {
    return map.get(shortUrl.substring(base.length()));
  }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
